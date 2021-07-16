import random, math, base64
import sys
import design
from PyQt5 import QtWidgets

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.encodeButton.clicked.connect(self.encode)
		self.decodeButton.clicked.connect(self.decode)
		self.keysButton.clicked.connect(self.key_generation)
	def encode(self):
		try:
			p = int(self.pField.toPlainText())
			g = int(self.gField.toPlainText())
			y = int(self.yField.toPlainText())
		except ValueError:
			self.encodeField.clear()
			self.encodeField.insertPlainText('Ошибка. Введите верный ключ\n')
		data = self.inputField.toPlainText()
		if data == '':
			self.encodeField.insertPlainText('Ошибка. Нечего шифровать. Введите данные')
		else:
			try:
				cypher = elgamal_encode(data, p, g, y)
				self.encodeField.clear()
				self.encodeField.insertPlainText(cypher)
			except BaseException:
				self.encodeField.clear()
				self.encodeField.insertPlainText("Ошибка")
	def decode(self):
		try:
			p = int(self.pField.toPlainText())
			x = int(self.xField.toPlainText())
		except ValueError:
			self.decodeField.clear()
			self.decodeField.insertPlainText('Ошибка. Введите верный ключ')
		data = self.encodeField.toPlainText()
		if data == '':
			self.encodeField.clear()
			self.encodeField.insertPlainText('Ошибка. Нечего расшифровывать. Зашифруйте что-нибудь')
		else:
			try:
				decoded_data = elgamal_decode(data, x, p)
				self.decodeField.clear()
				self.decodeField.insertPlainText(decoded_data)
			except BaseException:
				self.decodeField.clear()
				self.decodeField.insertPlainText("Ошибка")
	def key_generation(self):
#		self.decodeField.clear()
#		self.decodeField.insertPlainText('Пожалуйста подождите. Идет генерация ключей.')
		p, g, x, y = keys_gen()
		self.pField.clear()
		self.pField.insertPlainText(str(p))
		self.gField.clear()
		self.gField.insertPlainText(str(g))
		self.yField.clear()
		self.yField.insertPlainText(str(y))
		self.xField.clear()
		self.xField.insertPlainText(str(x))
#		self.decodeField.clear()


def main():
	app = QtWidgets.QApplication(sys.argv)
	window = ExampleApp()
	window.show() 
	app.exec_()




def gcd(a, b): 
	while a != 0 and b != 0:
		if a > b:
			a %= b
		else:
			b %= a
	return a + b


def primitive_root(modulo):
    res = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1,modulo))
        if required_set == actual_set:
            res.append(g)
            if len(res) > 10:
                return res

def mod_exp(base, exponent, modulus):
	result = 1
	while exponent > 0:
		if (exponent & 1) == 1:
			result = (result * base) % modulus
		exponent >>= 1
		base = (base * base) % modulus
	return result

def is_prime(number, rounds):
	if number < 2:
		return False
	if number == 2:
		return True
	if number % 2 == 0:
		return False
	s = number - 1
	r = 0
	while s % 2 == 0:
		r += 1
		s /= 2
	while rounds:
		a = random.randint(2, number - 2)
		s = int(s)
		if mod_exp(a, s, number) != 1:
			for j in range(0, r):
				if mod_exp(a, (2**j)*s, number) == number-1:
					break
			else:
				return False
		rounds -= 1
		continue
	return True

def keygen(p):
	x =  random.randint(10, p - 1)
	while (gcd(p -1, x) != 1):
		x =  random.randint(10, p - 1)
	return x

def make_uchr(code: str):
	return chr(int(code.lstrip("U+").zfill(8), 16))

def elgamal_encode(data, p, g, y):
	coded_res = ''
	res = []
	k = random.randint(10, (p - 1))
	while gcd(k, p - 1) != 1:
		k = random.randint(10, (p - 1))
	for i in range(len(data)):
		a = pow(g, k, p)
		b = pow(y, k)*ord(data[i]) % p
		res.append(str(a))
		res.append(str(b))
	for byte in res:
		tmp = 'U+'+ '0'* (4-len(hex(int(byte))[2:])) + hex(int(byte))[2:]
		t1 = make_uchr(tmp)
		coded_res += t1
	string = coded_res.encode()
	sr = base64.b64encode(string).decode()
	return sr

def keys_gen():
	p = random.randint(1700, 2000)
	while not is_prime(p, int(math.log2(p))):
		p = random.randint(1700, 2000)
	primitive_roots = primitive_root(p)
	g = random.choice(primitive_roots)
	x = keygen(p)
	y = pow(g, x, p)
	return p, g, x, y 

def elgamal_decode(msg, x, p):
	res = ''
	data = msg.encode()
	data = base64.b64decode(data).decode()
	for i in range(len(data)//2):
		a = ord(data[2*i])
		b = ord(data[2*i+1])
		decoded = ((b * pow(a, p - x -1)) % p)
		res += chr(decoded)
	return res

if __name__ == "__main__":
	main()
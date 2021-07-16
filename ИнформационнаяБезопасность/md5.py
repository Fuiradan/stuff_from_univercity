'''
import sys
from PyQt5 import QtWidgets
import md5_design
'''
import math
'''
class ExampleApp(QtWidgets.QMainWindow, md5_design.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.create_hash)
	
	def create_hash(self):
		self.outputField.clear()
		data = self.textEdit.toPlainText()
		n_data = flow_alignment(data)
		calculating(n_data)
		result = print_res()
		self.outputField.insertPlainText(result)

def main():
	app = QtWidgets.QApplication(sys.argv)
	window = ExampleApp()
	window.show()
	app.exec_()
'''
a0 = 0
b0 = 0
c0 = 0
d0 = 0

X = []

sh = [
7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21
]

T = [int(abs(math.sin(i+1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

def flow_alignment(string):
	tmp = '1'
	byte_str = strtobytes(string)
	res = []
	t1 = []
	t2 = []
	bit_length = len(byte_str) * 8
	extend_length = bit_length + 1
	if (extend_length % 512 == 448):
		trigger = True
	while (extend_length % 512 != 448) or trigger:
		trigger = False
		tmp +='0'
		extend_length += 1
		if len(tmp) == 8:
			h_tmp = hex(int(tmp, base=2))[2:]
			h_tmp = (2-len(h_tmp)) * '0' + h_tmp
			res.append(h_tmp)
			tmp = ''
	adding_length = bin(bit_length % pow(2, 64))[2:]
	adding_length = (64-len(adding_length)) * '0' + adding_length
	tmp += adding_length  
	for i in range(8):
		h_tmp = hex(int(tmp[8*i:8*(i+1)], base=2))[2:]
		h_tmp = (2-len(h_tmp)) * '0' + h_tmp
		if (i < 4):
			t1 = [h_tmp] + t1
		else:
			t2 = [h_tmp] + t2

	res = byte_str + res + t2 + t1
	return res

def strtobytes(string):
	res = []
	for symbol in string:
		code = ord(symbol)
		if code < 128:
			h_code = (2-len(hex(code)[2:])) * '0' + hex(code)[2:]
			res.append(h_code)
		else:
			t1 = int('110' + bin(code)[2:7], base = 2)
			t2 = int('10' + bin(code)[7:13], base = 2)
			res.append(hex(t1)[2:])
			res.append(hex(t2)[2:])
	return res


def rotate_left(num, s):
	num &= 0xFFFFFFFF
	return ((num<<s) | (num>>(32-s))) & 0xFFFFFFFF

def stringtobytes(string):
	byte = int(string, base= 16) 
	res = byte.to_bytes(4,byteorder="big")
	return res

def calculating(data):
	global X, a0, b0, c0, d0
	a0 = 0x67452301
	b0 = 0xefcdab89
	c0 = 0x98badcfe
	d0 = 0x10325476
	chunk_amount = len(data)//64
	for i in range(chunk_amount):
		chunk = data[64*i:64*(i+1)]
		f = 0
		g = 0
		A = a0
		B = b0
		C = c0
		D = d0
		X = [ (chunk[4*j] + chunk[4*j+1] + chunk[4*j+2] + chunk[4*j+ 3])  for j in range(16)]
		for j in range(64):
			if j <= 15:
				f = (B & C) | ((~B) & D)
				g = j
			elif (j >=16) and (j <= 31):
				f = (D & B) | ((~D) & C)
				g = (5*j + 1) % 16
			elif (j >= 32) and (j <= 47):
				f = B ^ C ^ D
				g = (3*j + 5) % 16
			elif (j >= 48) and (j <= 63):
				f = C ^ (B | (~D))
				g = (7*j) % 16
			f = (f + A + T[j] + (int.from_bytes(stringtobytes(X[g]), byteorder="little")))  &0xFFFFFFFF
			A = D
			D = C
			C = B
			B = (B + rotate_left(f, sh[j]))&0xFFFFFFFF

		a0 = (a0 + A) & 0xFFFFFFFF
		b0 = (b0 + B) & 0xFFFFFFFF
		c0 = (c0 + C) & 0xFFFFFFFF
		d0 = (d0 + D) & 0xFFFFFFFF


def print_res():
	global a0, b0, c0, d0
	hash_md5 = ''
	mas = ["{:08x}".format(a0), "{:08x}".format(b0), "{:08x}".format(c0), "{:08x}".format(d0)]
	for h in mas:
		tmp = h[6:8] + h[4:6] + h[2:4] + h[0:2]
		hash_md5 += tmp
	return hash_md5

'''
s = 'ывфар2842  38н8раыфао'
'''
def create_md5(data):
	a_s = flow_alignment(data)
	calculating(a_s)
	result = print_res()
	return (result)

'''
if __name__ == '__main__':
    main()
'''	
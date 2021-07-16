from PyQt5 import QtWidgets
import design, sys

tabula_recta = 0
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 'LEMON'

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.encodeButton.clicked.connect(self.start_encode)
		self.decodeButton.clicked.connect(self.start_decode)
	def start_encode(self):
		global tabula_recta
		self.outputField.clear()
		data = self.inputField.toPlainText().replace(' ', '').upper()
		key = self.keyField.toPlainText().replace(' ', '').upper()
		tabula_recta = create_matrix(key)
		result = encode(data)
		self.outputField.insertPlainText(result)
	def start_decode(self):
		global tabula_recta
		self.outputField.clear()
		data = self.inputField.toPlainText().replace(' ', '').upper()
		key = self.keyField.toPlainText().replace(' ', '').upper()
		tabula_recta = create_matrix(key)
		result = decode(data)
		self.outputField.insertPlainText(result)


def main():
	app = QtWidgets.QApplication(sys.argv)
	window = ExampleApp()
	window.show() 
	app.exec_()

def create_matrix(key):
	global alphabet
	res = ['', alphabet]
	for symbol in key:
		if not (symbol in res[0]):
			res[0] += symbol
			tmp =  alphabet.split(symbol)
			tmp = symbol + tmp[1] + tmp[0]
			res.append(tmp)
	return res

def encode(string):
	global tabula_recta, key
	res = ''
	len_str = len(string)
	len_key = len(key)
	if len_str > len_key:
		key_s = (len_str // len_key) * key + key[:len_str % len_key]
	else:
		key_s = key[:len_str]
	for i in range(len_str):
		pos1 = tabula_recta[1].index(string[i])
		pos2 = tabula_recta[0].index(key_s[i])
		res += tabula_recta[pos2+2][pos1]
	return res

def decode(string):
	global tabula_recta, key
	res = ''
	len_str = len(string)
	len_key = len(key)
	if len_str > len_key:
		key_s = (len_str // len_key) * key + key[:len_str % len_key]
	else:
		key_s = key[:len_str]
	for i in range(len_str):
		pos_key_s = tabula_recta[0].index(key_s[i])
		pos1 = tabula_recta[pos_key_s+2].index(string[i])
		res += tabula_recta[1][pos1]
	return res

if __name__ == '__main__':
	main()
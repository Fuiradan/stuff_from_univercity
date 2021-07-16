import sys, design
from PyQt5 import QtWidgets

class ExampleApp(QtWidgets.QMainWindow, design.Ui_mainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.encode)
		self.pushButton_2.clicked.connect(self.decode)
	def encode(self):
		data = self.textEdit.toPlainText()
		res = coding(data)
		self.textEdit_2.clear()
		self.textEdit_2.insertPlainText(res)
	def decode(self):
		data = self.textEdit.toPlainText()
		res = decoding(data)
		self.textEdit_2.clear()
		self.textEdit_2.insertPlainText(res)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

def coding(string):
	res = ''
	for symbol in string:
		tmp = chr(ord(symbol) - 5)
		res += tmp
	return res

def decoding(string):	
	res = ''
	for symbol in string:
		tmp = chr(ord(symbol) + 5)
		res += tmp
	return res



if __name__ == '__main__':
    main()


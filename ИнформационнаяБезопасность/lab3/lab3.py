import base64, sys, design
from PyQt5 import QtWidgets

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.start_work)
	def start_work(self):
		global nk, nr
		self.OutputField.clear()
		work_type = str(self.ChooseWorkType.currentText())
		aes_type = str(self.AESTypeBox.currentText())
		if aes_type == 'AES-128':
			nk = 4
			nr = 10
		elif aes_type == 'AES-192':
			nk = 6
			nr = 12
		else:
			nk = 8
			nr = 14
		data = self.InputField.toPlainText()
		key = self.KeyField.toPlainText()
		if len(key) == nk * 4:
			try:
				result = aes_main(data, key, work_type)
				result = print_res(result, work_type)
			except BaseException:
				result = "Ошибка"
		else:
			result = 'Неверная длина ключа. Введите ключ длиной {}'.format(nk * 4)
		self.OutputField.insertPlainText(result)






nb = 4
nk = 0
nr = 0
state = []

s_box = [
[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
[0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
[0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
[0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
[0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
[0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
[0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
[0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
[0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
[0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
[0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
[0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
[0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
[0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
[0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
[0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
]

rcon = [
[0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36],
[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
]

invs_box = [
[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
[0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
[0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
[0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
[0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
[0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
[0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
[0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
[0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
[0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
[0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
[0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
[0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
[0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
[0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
[0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
]

def sub_bytes(state, inv = False):
	if inv == False:
		box = s_box
	else:
		box = invs_box

	for i in range(len(state)):
		for j in range(len(state[i])):
			row = state[i][j] // 0x10
			column = state[i][j] % 0x10
			box_element = box[row][column]
			state[i][j] = box_element

	return state

def shift_rows(state, inv = False):
	count = 1
	if inv == False:
		for i in range(1,len(state)):
			state[i] = left_shift(state[i], count)
			count += 1
	else:
		for i in range(1,len(state)):
			state[i] = right_shift(state[i], count)
			count += 1
	return state

def left_shift(row, count):
	tmp = []
	for i in range(count):
		byte = row.pop(0)
		tmp.append(byte)
	res = row + tmp
	return res

def right_shift(row, count):
	tmp = []
	for i in range(count):
		byte = row.pop(len(row)-1)
		tmp = [byte] + tmp
	res = tmp + row
	return res

def mix_columns(state, inv = False):
	for i in range(nb):
		if inv == False:
			s0 = m02(state[0][i]) ^ m03(state[1][i]) ^ state[2][i] ^ state[3][i]
			s1 = state[0][i] ^ m02(state[1][i]) ^ m03(state[2][i]) ^ state[3][i]
			s2 = state[0][i] ^ state[1][i] ^ m02(state[2][i]) ^ m03(state[3][i])
			s3 = m03(state[0][i]) ^ state[1][i] ^ state[2][i] ^ m02(state[3][i])
		else:
			s0 = m0e(state[0][i]) ^ m0b(state[1][i]) ^ m0d(state[2][i]) ^ m09(state[3][i])
			s1 = m09(state[0][i]) ^ m0e(state[1][i]) ^ m0b(state[2][i]) ^ m0d(state[3][i])
			s2 = m0d(state[0][i]) ^ m09(state[1][i]) ^ m0e(state[2][i]) ^ m0b(state[3][i])
			s3 = m0b(state[0][i]) ^ m0d(state[1][i]) ^ m09(state[2][i]) ^ m0e(state[3][i])
		
		state[0][i] = s0
		state[1][i] = s1
		state[2][i] = s2
		state[3][i] = s3

	return state


def add_round_key(state, key_schedule, round = 0):
	for column in range(nb):
		s0 = state[0][column] ^ key_schedule[0][nb * round + column]
		s1 = state[1][column] ^ key_schedule[1][nb * round + column]
		s2 = state[2][column] ^ key_schedule[2][nb * round + column]
		s3 = state[3][column] ^ key_schedule[3][nb * round + column]
		state[0][column] = s0
		state[1][column] = s1
		state[2][column] = s2
		state[3][column] = s3
	

	return state
	

def key_expansion(key):
	k_bytes = [symbol for symbol in key]
	if len(k_bytes) < (4* nk):
		for i in range(4*nk - len(k_bytes)):
			k_bytes.append(0x01)
	key_schedule = [[] for i in range(4)]
	for r in range(4):
		for c in range(nk):
			key_schedule[r].append(k_bytes[r + 4*c]) 
	for column in range(nk, nb * (nr + 1)):
		if column % nk == 0:
			tmp = [key_schedule[row][column - 1] for row in range(1, 4)]
			tmp.append(key_schedule[0][column - 1])
			for j in range(len(tmp)):
				box_row = tmp[j] // 0x10
				box_col = tmp[j] % 0x10
				box_element = s_box[box_row][box_col]
				tmp[j] = box_element
			for row in range(4):
				s = key_schedule[row][column - nk] ^ tmp[row] ^ rcon[row][int(column / nk) - 1]
				key_schedule[row].append(s)
		elif (column % nk == 4) and (nk == 8):
			tmp = [key_schedule[row][column - 1] for row in range(0, 4)]
			for j in range(len(tmp)):
				box_row = tmp[j] // 0x10
				box_col = tmp[j] % 0x10
				box_element = s_box[box_row][box_col]
				tmp[j] = box_element
			for row in range(4):
				s = key_schedule[row][column - nk] ^ tmp[row]
				key_schedule[row].append(s)
		else:
			for row in range(4):
				s = key_schedule[row][column - nk] ^ key_schedule[row][column - 1]
				key_schedule[row].append(s)
	return key_schedule


def encode(input_data, key):
	state = [[] for j in range(4)]
	for r in range(4):
		for c in range(nb):
			state[r].append(input_data[r+4*c])
	
	
	key_schedule = key_expansion(key)
#	print_key(key_schedule)
	state = add_round_key(state, key_schedule)

	for round in range(1, nr):
		state = sub_bytes(state)
		state = shift_rows(state)
		state = mix_columns(state)
		state = add_round_key(state, key_schedule, round)
	state = sub_bytes(state)
	state = shift_rows(state)
	state = add_round_key(state, key_schedule, round + 1)

	output = [None for i in range(4 * nb)]
	for r in range(4):
		for c in range(nb):
			output[r + 4 * c] = state[r][c]
	return output

def decode(input_data, key):
	state = [[] for j in range(4)]
	for r in range(4):
		for c in range(nb):
			state[r].append(input_data[r+4*c])
	
	key_schedule = key_expansion(key)
	state = add_round_key(state, key_schedule, nr)
	round = nr - 1
	while round >= 1:
		state = shift_rows(state, inv=True)
		state = sub_bytes(state, inv=True)
		state = add_round_key(state, key_schedule, round)
		state = mix_columns(state, inv=True)
		round -= 1
	
	state = shift_rows(state, inv=True)
	state = sub_bytes(state, inv=True)
	state = add_round_key(state, key_schedule, round)
	
	output = [None for i in range(4 * nb)]
	for r in range(4):
		for c in range(nb):
			output[r + 4 * c] = state[r][c]
	return output
		

def print_key(key_m):
	t = ''
	for i in range(nb * (nr + 1)):
		for j in range(4):
			byte = "{:02x}".format(key_m[j][i])
			t += '' + byte
			if len(t) == 32:
				print(t, '\n')
				t = ''
			


def m02(num):
	if num < 0x80:
		res = (num << 1)
	else:
		res = (num << 1) ^ 0x1b
	return res % 0x100


def m03(num):
	return (m02(num) ^ num)


def m09(num):
	return m02(m02(m02(num))) ^ num


def m0b(num):
	return m02(m02(m02(num))) ^ m02(num) ^ num


def m0d(num):
	return m02(m02(m02(num))) ^ m02(m02(num)) ^ num


def m0e(num):
	return m02(m02(m02(num))) ^ m02(m02(num)) ^ m02(num)

def aes_main(input_data, key, work_type):
	if work_type == 'Шифрование':
		s = input_data.encode('utf-8')
		key = key.encode('utf-8')
	if work_type == 'Дешифрование':
		s = base64.b64decode(input_data)
#		s = s + b'='* (len(s) % 4)
		key = key.encode('utf-8')
	res_data = []
	words_amount = len(s) // 16
	for i in range(words_amount):
		if work_type == 'Шифрование':
			tmp = encode(s[16*i:16*(i+1)], key)
			res_data += tmp 
		if work_type == 'Дешифрование':
			tmp = decode(s[16*i:16*(i+1)], key)
			res_data += tmp
		s = s[16*(i+1):]
	if (s != b'') and (work_type == 'Шифрование'):
		s = s + b'\x80' + (16-len(s) + 2) * b'\x00'
		tmp = encode(s, key)
		res_data += tmp 

	return res_data

def print_res(mas, work_type):
	bytestring = b''
	for byte in mas:
		symbol = bytes([byte])
		bytestring += symbol
	if work_type == 'Шифрование':
		string = base64.b64encode(bytestring).decode('utf-8')
	if work_type == 'Дешифрование':
		index = bytestring.find(b'\x80')
		bytestring = bytestring[:index]
		string = bytestring.decode()
	return string


#work_type = 'encrypt'
#inp = b'\x32\x43\xF6\xA8\x88\x5A\x30\x8D\x31\x31\x98\xA2\xE0\x37\x07\x34'
#inp = 'qwerty'
#key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17'
#input_string = input().encode()
#key = input().encode()
#inp = [byte for byte in input_string]
#k = encode(inp, key)
#print(k)
#ek = decode(k, key)
#print(ek)
#res = aes_main(inp, key, work_type)
#r = print_res(res, work_type)
#print(r)


def main():
	app = QtWidgets.QApplication(sys.argv)
	window = ExampleApp()
	window.show() 
	app.exec_()

if __name__ == '__main__':
	main()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 'LEMON'


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





str = input().replace(' ', '').upper()
tabula_recta = create_matrix(key)
t = encode(str)
print(t)
t1 = decode(t)
print(t1)
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


s = input()
r = coding(s)
r1 = decoding(r)
print(r)
print(r1)
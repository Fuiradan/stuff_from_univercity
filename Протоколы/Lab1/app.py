import subprocess

sp_return = subprocess.Popen("hostname", shell=True, stdout=subprocess.PIPE)
print('Hostname:', sp_return.stdout.read().decode('utf-8'))
sp_return = subprocess.Popen("ifconfig", shell=True, stdout=subprocess.PIPE)
print('IPv4 list:')
trigger = True
for line in sp_return.stdout:
    line_words = line.split()
    if b'inet' in line_words:
        trigger = False
        print (line_words[1].decode('utf-8'), end= '\n')
if trigger:
    print("Not found")
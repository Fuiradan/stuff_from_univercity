import pika
import threading
import socket
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='hub.zaikin.su', credentials=pika.PlainCredentials('guest', 'surgu2019')))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)

server = '127.0.0.1', 8080
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0))

name = input('Введите логин: ')

def send():
	while True:
		mes_time = time.asctime()
		message = '[' + mes_time + ']'+name+': ' + input()
		channel.basic_publish(exchange='logs', routing_key='', body=message)

def read_sok():
	while True :
		data = sor.recv(1024)
		print(data.decode('utf-8'))

def pull_name(login):
    sor.sendto(login.encode('utf-8'),server)

pull_name(name)

potok_server = threading.Thread(target= read_sok)
potok_server.start()
   
potok = threading.Thread(target= send)
potok.start()
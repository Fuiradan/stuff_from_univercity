import socket
import sys
import pika
import threading
import re

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='hub.zaikin.su', credentials=pika.PlainCredentials('guest', 'surgu2019')))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',8080))
client = []
client_name = []
client_name_id = {}

def callback(ch, method, properties, body):
    global client, client_name, client_name_id
    body = str(body).replace("b", '')
    body = body.replace("'", '')
    pattern = re.compile(r'\w+')
    pattern = pattern.findall(body)
    print(pattern)
    if body[body.find("@")+1:] == "who_are_here?":
        for clients in client:
            for name in client_name:
                sock.sendto(("[{}] i'm HERE!".format(name)).encode('utf-8'), clients)
    elif pattern in client_name:
        for name in client_name:
            if pattern == name:
                sock.sendto((body).encode('utf-8'), client_name_id[name])
    else:
        for clients in client: 
            sock.sendto(body.encode('utf-8'), clients)

def take_name():
    global client, client_name, client_name_id
    while True:
        data , addres = sock.recvfrom(1024)
        data = str(data).replace('b','')
        data = data.replace("'",'')       
        print (addres[0],addres[1])
        if addres not in client:
            client.append(addres)
            client_name.append(data)
            client_name_id[data] = addres
            for clients in client:
                sock.sendto(('{} зашел в чат'.format(data)).encode('utf-8'), clients)
        print(client)
        print(client_name)

potok_server = threading.Thread(target= take_name)
potok_server.start()

print('*** Server started ***')
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
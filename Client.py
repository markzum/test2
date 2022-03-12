# test-client.py
import socket

# СоздаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаем сокет к порту, через который прослушивается сервер
server_address = ('91.215.201.1', 10000) #localhost
#print('Подключено к {} порт {}'.format(*server_address))
sock.connect(server_address)

while True:
    try:
        # Отправка данных
        mess = input("Введите сообщение: ")
        if mess == "exit":
            sock.close()
            break
        else:
            message = mess.encode() #Закодировать
            sock.sendall(message)

    except:
        print('Закрываем сокет')
        sock.close()

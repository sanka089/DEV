server udp   from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', serverPort))
print('The server is ready to receive')

while True:
    sentence, clientAddress = serverSocket.recvfrom(2048)
    sentence = sentence.decode('utf-8')

    try:
        file = open(sentence, "r")
        content = file.read(2048)
        serverSocket.sendto(bytes(content, 'utf-8'), clientAddress)
        print('\nSent contents of', sentence)
        file.close()
    except FileNotFoundError:
        error_message = "File not found"
        serverSocket.sendto(bytes(error_message, 'utf-8'), clientAddress)
        print('\nFile not found:', sentence)

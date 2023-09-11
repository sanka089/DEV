client udp 
from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

try:
    sentence = input('\nEnter file name: ')
    clientSocket.sendto(bytes(sentence, 'utf-8'), (serverName, serverPort))
    filecontents, serverAddress = clientSocket.recvfrom(2048)

    if filecontents.decode('utf-8') == "File not found":
        print('\nFile not found on the server.')
    else:
        print('\nReply from Server:\n')
        print(filecontents.decode('utf-8'))

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    clientSocket.close()

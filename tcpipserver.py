Server.py from socket import *
serverName= '127.0.0.1'
serverPort= 12000
serverSocket= socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
while True:
    print("The Server is ready to receive")
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()

    try:
        file = open(sentence, "r")
        file_contents = file.read(1024)
        connectionSocket.send(file_contents.encode())
        print("\nSent contents of " + sentence)
        file.close()
    except FileNotFoundError:
        error_message = "File not found"
        connectionSocket.send(error_message.encode())

    connectionSocket.close()

from socket import *

serverPort = 12006
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is reader so receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    print(clientAddress)
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
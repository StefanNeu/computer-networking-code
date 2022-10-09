from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 28109
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print(f'Server is listening on port {serverPort} for new connection establishments...')
# Prepare a server socket

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()

        # send HTTP header that requested file was found
        connectionSocket.send('HTTP/1.1 200 OK'.encode())
        connectionSocket.send('Connection: close'.encode())
        connectionSocket.send("\n".encode())

        for line in outputdata:
            connectionSocket.send(line.encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        pass
        # Send response message for file not found
        # Fill in start
        # Fill in end
        # Close client socket
        # Fill in start
        # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data

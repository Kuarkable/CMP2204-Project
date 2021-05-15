from socket import *

serverPort = 12000

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the port
serverSocket.bind( ('', serverPort) )
print("The server is ready to receive")

while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	print('received {} bytes from {}'.format(len(message), clientAddress))
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)



def Open_UDPServer():
	pass

def Map_Chunk_Info(): #Will map the chunk-ip info.
	pass

def Check_Database(): #Will check the data for matching chunk-ip pairs
	pass

def Send_Chunk_Indo(): #Will send the corresponding chunk info to the client it it exists.
	pass


def hippo():
    print("hey m8")
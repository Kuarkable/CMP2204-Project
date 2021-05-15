import math
import os
from ServerScripts import UdpServer, UdpClient, TcpServer, TcpClient

content_name = ""
filename = ""

def get_file_name():
    content_name = input("Please enter the name of the file you would like to download.")
    filename = content_name + ".png"


def get_file_size(filename):
    filesize = os.path.getsize(filename)
    print("Your file is ", filesize, "kbs.")
    CHUNK_SIZE = math.ceil(math.ceil(filesize) / 5)
    print("Your file is ", CHUNK_SIZE, " chunks.")


while 1:

    # Opening the servers and clients.

    UdpServer.Open_UDPServer()
    TcpServer.Open_TCPServer()
    UdpClient.Open_UDPClient()
    TcpClient.Open_TCPClient()

    UdpClient.Send_Uploadable_Chunk_Info()

    print("Searching for your file in the system.")
    UdpServer.Check_Database() #Will search the name of the specified file in the system to check if its available. If it is it'll map the chunks and ips.
    TcpClient.Open_TCPClient() #Will open the client if the requested chunks exists.
    TcpClient.Form_Connections() #Will form the connections to the mapped ips.
    TcpClient.Download_Chunks()



UdpServer.hippo()
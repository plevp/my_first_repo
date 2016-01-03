
import socket
import urllib

def main1():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect( ('www.py4inf.com', 80));


    my_socket.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

    while True:
        data = my_socket.recv(512)
        if (len(data) <1 ):
            break
        print data
    my_socket.close()


def main2():

    url = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

    for line in url:
        print line.strip()
    
    
#main1()
main2()




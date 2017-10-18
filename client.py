#!/usr/bin/env python
# coding: utf-8



def client_send_data(host,port,data):

    import socket
    hote = host
    ports =port

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((hote, port))
    print("Connection on {}".format(port))


    socket.send(data.encode())

    print("Close")
    socket.close()



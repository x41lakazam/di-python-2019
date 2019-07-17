###########################################
###  *              *              *    ###
###       *      *        *    *        ###
###    *                    *    *      ###
###           *    CLIENT               ###
###                                     ###
###                                     ###
###########################################
import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect(('192.168.31.98', 45636))

msg = socket.recv(4096)
print("Received from server: {}".format(msg.decode('utf-8')))

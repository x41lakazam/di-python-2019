import socket


def client_handler(client_socket, client_ip):
    client_socket.send("Hello my friend".encode('utf-8'))
    while True:
        received = client_socket.recv(4096)
        received_s = received.decode('utf-8')
        if len(received_s.strip()) > 0:
            print("Client said: {}".format(received_s))

# Create a pipe
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

bind_addr = '0.0.0.0'
bind_port = 876

socket.bind((bind_addr, bind_port))

socket.listen(5)
print("[*] Listening on {}:{}".format(bind_addr, bind_port))

client_socket, client_address = socket.accept()
print("[*] Connected to",client_address)

client_handler(client_socket, client_address)







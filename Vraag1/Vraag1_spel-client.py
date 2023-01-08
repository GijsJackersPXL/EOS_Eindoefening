import socket

# Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the socket to non-blocking mode
client_socket.setblocking(0)

# Send a message to the server
client_socket.sendto(b'4', ('192.168.0.178', 8000))

#testint = int(b'a')
#print(type(testint))

while True:
    try:
        # Receive data from the server
        data, address = client_socket.recvfrom(4096)
        print(f'Received message from {address}: {data}')
    except:
        # No data was received, pass this iteration of the loop
        pass
import socket

HOST, PORT = '0.0.0.0', 1234

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    request = request.decode("utf-8")
    print(request)
    http_response = "author @w0x7ce \n" + request
    client_connection.sendall(http_response.encode("utf-8"))
    client_connection.close()

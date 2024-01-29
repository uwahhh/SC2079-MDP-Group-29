import socket


class RPIServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket, self.client_socket, self.client_address = None, None, None

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        print(f"Server listening on {self.host}:{self.port}")
        self.socket.listen()

        # Accept connection from a client
        self.client_socket, self.client_address = self.socket.accept()
        print(f"Connected to {self.client_address}")

    def receive_data(self):
        data = self.client_socket.recv(1024)
        return data.decode('utf-8')

    def send_data(self, data):
        self.client_socket.sendall(data.encode('utf-8'))

    def close(self):
        print("Ending connection.")
        self.socket.close()

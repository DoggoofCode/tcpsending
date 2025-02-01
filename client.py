import socket

def send_data(host='srv.vedjaggi.com', port=42595, message='Hello, Server!'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    send_data(message="gadagadegadagadago")

import socket
import threading

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received data from {addr}: {data}")
            sending_data = f"I believe you send: {data.decode()}. I hope I am correct!"
            conn.sendall(sending_data.encode())
    print(f"Connection with {addr} closed")

def start_server(host='0.0.0.0', port=42595):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    start_server()

from os import environ, config
import socket


PORT = int(environ.get("PORT"))  # server_config.getint('PORT')


def start_tcp_server(ip, port):
    # Create a socket object using the AF_INET address family and SOCK_STREAM type
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the specified IP address and port number
    server_socket.bind((ip, port))

    # Start listening for incoming connections, with a specified backlog of 5
    server_socket.listen(5)
    print(f"Server started on {ip} port {port}. Waiting for connections...")

    try:
        while True:
            # Accept a new connection
            client_socket, addr = server_socket.accept()
            print(f"Connected to {addr}")

            # Handle the client connection in a separate function or here directly
            handle_client(client_socket)

    except KeyboardInterrupt:
        print("Server is shutting down.")

    finally:
        # Close the server socket to free the port and resources
        server_socket.close()
        print("Server socket closed.")


def handle_client(client_socket):
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break  # Exit if no data is received

            # Print received data
            decoded_data = [byte for byte in data]
            print(f"Received from client: {decoded_data}")

    except Exception as e:
        print(f"Error handling client: {e}")

    finally:
        client_socket.close()
        print("Client connection closed.")


# Start the server
start_tcp_server("0.0.0.0", PORT)

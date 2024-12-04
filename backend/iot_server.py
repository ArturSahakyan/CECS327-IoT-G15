import socket
import ipaddress

"""
    MSG Codes:
        1 - Avg moisture inside kitchen fridge
        2 - Avg water consumption per cycle in dishwasher
        3 - Which device consumed more electricity
"""

MAX_CONNECTIONS = 5
RECV_BYTES = 1024

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(MAX_CONNECTIONS)

        while True:
            client_socket, address = server_socket.accept()
            with client_socket:
                while True:
                    msg = client_socket.recv(RECV_BYTES)
                    if not msg:
                        break
                    # Message will always be valid

                    resp = msg.decode().upper()
                    client_socket.sendall(resp.encode())

if __name__ == "__main__":
    host_ip = "0.0.0.0" 
    try:
        ipaddress.ip_address(host_ip)
    except ValueError:
        print("Invalid IP Address..")
        exit()

    try:
        host_port = int(input("Enter host port: "))
        if host_port < 1 or host_port > 65535:
            raise ValueError()
    except ValueError:
            print("Invalid Port")
            exit()

    start_server(host_ip, host_port)

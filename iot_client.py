import socket
import ipaddress

RECV_BYTES = 1024

"""
    MSG Codes:
        1 - Avg moisture inside kitchen fridge
        2 - Avg water consumption per cycle in dishwasher
        3 - Which device consumed more electricity
"""

def c_menu() -> int:
    print("\nPlease Pick One (Type 1, 2, or 3)")
    print("\t1. What is the average moisture inside my " 
          "kitchen fridge in the past three hours?")
    print("\t2. What is the average water consumption "
          "per cycle in my smart dishwasher?")
    print("\t3. Which device consumed more electricity "
          "among my three IoT devices?")

    usr = -1 
    try:
        usr = int(input("\n> ")) 
    except ValueError as e:
        print("\nPlease type just the number 1, 2, or 3\n")
        usr = -1

    return usr

def start_client():
    while True:
        ip = input("Enter IP: ")
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            print("Invalid IP")
            continue

        try:
            port = int(input("Enter Port: "))
            if port < 1 or port > 65535:
                raise ValueError()
        except ValueError:
            print("Port Number Wrong")
            continue

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((ip, port))
            except (socket.error, ConnectionRefusedError) as e:
                print(f"Error {e}")
                continue

            while True:
                usr = c_menu() 
                while usr < 1 or usr > 3:
                    print("\nInvalid Input")
                    usr = c_menu()

                client_socket.sendall(str(usr).encode())
                resp = client_socket.recv(RECV_BYTES)
                print(f"Server Responded: {resp.decode()}")

if __name__ == "__main__":
    start_client()

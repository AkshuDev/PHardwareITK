import socket
import sys

def main():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            data = s.recv(1024)
            if not data:
                print("Disconnected from server.")
                break
            print(data.decode(), end='')
            cmd = input()
            s.sendall(cmd.encode() + b"\n")
            if cmd.strip() == "exit":
                break

if __name__ == "__main__":
    main()

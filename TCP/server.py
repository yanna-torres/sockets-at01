import socket
from convert_currency import convert_currency

HOST = '127.0.0.1'
PORT = 65432


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss: # ss = server socket
        ss.bind((HOST, PORT))
        ss.listen()
        conn, addr = ss.accept()
        with conn:
            print('Connected by', addr)
            try:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    value, currency = data.decode().split('|')
                    result = convert_currency(float(value), currency)
                    conn.sendall(str(result).encode())
            finally:
                conn.close()




if __name__ == '__main__':
    main()
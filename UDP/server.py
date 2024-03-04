import socket

from utils import convert_currency

HOST = '127.0.0.2'
PORT = 65433

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as ss: # ss = server socket
        ss.bind((HOST, PORT))
        while True:
            data, addr = ss.recvfrom(1024)
            value, currency = data.decode().split('|')
            result = convert_currency(float(value), currency)
            ss.sendto(str(result).encode(), addr)

if __name__ == '__main__':
    main()
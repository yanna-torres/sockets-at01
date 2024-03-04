import socket
import inquirer

HOST = '127.0.0.1'
PORT = 65432

CURRENCIES = ['USD', 'EUR', 'GBP', 'JPY']
questions = [
    inquirer.Text('value', message='Enter the value to be converted (R$): '),
    inquirer.List('currency', message='Enter the currency to convert:', choices=CURRENCIES)
]

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs: # cs = client socket
        cs.connect((HOST, PORT))
        while True:
            aws = inquirer.prompt(questions)
            message = f"{aws['value']}|{aws['currency']}"
            cs.sendall(message.encode())

            data, _ = cs.recvfrom(1024)
            print(f"Converted value: {data.decode()}")

if __name__ == '__main__':
    main()
import socket
import inquirer

HOST = '127.0.0.2'
PORT = 65433

CURRENCIES = ['USD', 'EUR', 'GBP', 'JPY']
questions = [
    inquirer.Text('value', message='Enter the value to be converted (R$): '),
    inquirer.List('currency', message='Enter the currency to convert:', choices=CURRENCIES)
]

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cs: # cs = client socket
        while True:
            aws = inquirer.prompt(questions)
            message = f"{aws['value']}|{aws['currency']}"
            cs.sendto(message.encode(), (HOST, PORT))

            data, _ = cs.recvfrom(1024)
            print(f"Converted value: {data.decode()}")

if __name__ == '__main__':
    main()
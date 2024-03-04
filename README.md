# Conversor de Moedas - Cliente e Servidor Socket em Python :globe_with_meridians:

Este projeto consiste em um aplicativo cliente e servidor implementados em Python, utilizando tanto UDP quanto TCP para comunicação. O objetivo é criar um conversor de moedas simples, onde o cliente envia um valor em reais (R$) e a moeda desejada para o servidor, que então retorna o valor convertido com base na cotação atual da moeda.

## Funcionalidades :clipboard:
- Aplicativo cliente que permite ao usuário inserir um valor em reais e a moeda desejada.
- Aplicativo servidor que recebe a solicitação do cliente, calcula a conversão com base na cotação do dia 04/03/2024 e envia o resultado de volta ao cliente.
- Implementações separadas usando UDP e TCP para a comunicação entre cliente e servidor.

## Requisitos :scroll:
- Python 3.x
- requirements.txt

## Instalando :woman_technologist:

1. Clonando o repositório:
   ```bash
   git clone https://github.com/yanna-torres/sockets-at01.git
   ```
2. Navegue até o repositório:
   ```bash
   cd sockets-at01
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Usar :play_or_pause_button:

1. **Execute o Servidor:**
    - Execute `UDP/server.py` ou `TCP/server.py` dependendo do protocolo que deseja utilizar.
    ```bash
    python UDP/server.py
    ```
    ou
    ```bash
    python TCP/server.py
    ```

2. **Execute o Cliente:**
    - Execute `UDP/client.py` ou `TCP/client.py` dependendo do protocolo que deseja utilizar.
    ```bash
    python UDP/client.py
    ```
    ou
    ```bash
    python TCP/client.py
    ```

3. **Siga as Instruções no Console:**
    - No cliente, siga as instruções fornecidas para inserir o valor em reais e selecione a moeda desejada.

## Tutoriais Utilizados de Apoio :card_index_dividers:

- [Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)
- [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)
- [Creating a Simple Socket Server and Client in Python](https://youtu.be/sUzM-vIC-s4?si=-02PqvgNB51FoU3H)

## Autores
- [Gabriel Vasconcelos](https://github.com/Gabriel-Vasconcelos)
- [João Victor](https://github.com/joaoVictorBAlves)
- [Yanna Torres](https://github.com/yanna-torres)
import socket
from time import sleep

class Cliente:
    def __init__(self, host="127.0.0.1", porta=8080):
        self.host = host
        self.porta = porta
        self.conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.conexao.connect((self.host, self.porta))
        except ConnectionError:
            print("Erro: Não foi possível conectar ao servidor.")
            self.conexao = None

    def enviar_requisicao(self, consulta):
        if not self.conexao:
            return "Sem conexão com o servidor."

        try:
            requisicao = consulta.strip() + "\n"
            sleep(0.2)
            print(f"[DEBUG] Enviando: {requisicao.strip()}")
            self.conexao.sendall(requisicao.encode())

            resposta = self.conexao.recv(1024).decode()
            sleep(0.2)
            print("-=" * 50)
            sleep(0.2)
            return resposta
        except ConnectionError:
            return "Erro ao enviar a requisição."

    def desconectar(self):
        if self.conexao:
            try:
                self.conexao.sendall("QUIT\n".encode())
                self.conexao.close()
                self.conexao = None
            except ConnectionError:
                pass

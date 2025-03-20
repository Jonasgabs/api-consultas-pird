import socket
from time import sleep

class Cliente:
    def __init__(self, host="127.0.0.1", porta=8080):
        self.host = host
        self.porta = porta

    def enviar_requisicao(self, consulta):
      
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
                cliente.connect((self.host, self.porta))

                if consulta.isdigit():  
                    requisicao = f"SEARCH /{consulta}\n"
                else:
                    requisicao = f"SEARCH /{consulta.lower()}\n"

                sleep(0.5)
                print(f"[DEBUG] Enviando: {requisicao.strip()}")
                cliente.sendall(requisicao.encode())

                resposta = cliente.recv(1024).decode()
                sleep(0.5)
                print(f"[DEBUG] Resposta recebida: \n{resposta}")
                sleep(0.5)
                print("-=" * 50)
                sleep(0.5)
                return resposta
        except ConnectionError:
            return "Erro: Não foi possível conectar ao servidor."

    def desconectar(self):
        
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
                cliente.connect((self.host, self.porta))
                cliente.sendall("QUIT\n".encode())
        except ConnectionError:
            pass 

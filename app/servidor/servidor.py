import socket
import threading
import json
from ..models.database import PRODUTOS


class Servidor:
    def __init__(self, host="127.0.0.1", porta=8080):
        self.host = host
        self.porta = porta

        self.produtos = PRODUTOS

        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.bind((self.host, self.porta))
        self.servidor.listen(5)
        print(f"Servidor rodando em {self.host}:{self.porta}")

    def iniciar(self):
        while True:
            conn, addr = self.servidor.accept()
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

    def consultar_produtos(self, query):
        if isinstance(query, (int, float)):
            resultado = [produto.to_dict() for produto in self.produtos.values() if produto.preco == query]
            
            if resultado:
                return f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{json.dumps(resultado)}"
            else:
                return "HTTP/1.1 404 Not Found\n\nNenhum produto encontrado com esse preço."

        elif isinstance(query, str):
            produto = self.produtos.get(query.lower())
            if produto:
                return f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{json.dumps(produto.to_dict())}"
            else:
                return "HTTP/1.1 404 Not Found\n\nProduto não encontrado."

        return "HTTP/1.1 400 Bad Request\n\nConsulta inválida."

    def processar_requisicao(self, requisicao):
        linhas = requisicao.split("\n")

        if len(linhas) > 0:
            linha_req = linhas[0].split() 
            print(linha_req)  

            if len(linha_req) >= 2 and linha_req[0] == "SEARCH":
                recurso = linha_req[1].strip("/")  
                return self.consultar_produtos(recurso)
            elif linha_req[0] == "QUIT":
                return "HTTP/1.1 200 OK\n\nConexão encerrada."
            
        return "HTTP/1.1 400 Bad Request\n\nRequisição inválida"
    
    def handle_client(self, conn, addr):
        print(f"Cliente conectado: {addr}")
        data = conn.recv(1024).decode()

        if data:
            resposta = self.processar_requisicao(data)
            conn.sendall(resposta.encode())

        conn.close()

if __name__ == "__main__":
    servidor = Servidor()
    servidor.iniciar()

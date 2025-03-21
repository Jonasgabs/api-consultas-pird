import socket
import threading
import json
from app.models.database import PRODUTOS
from app.models.Produto import Produto


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
        query = query.lstrip("/")

        if query.replace('.', '', 1).isdigit():
            query = float(query)
            resultado = [produto.dicionario() for produto in self.produtos.values() if produto.preco == query]
            if resultado:
                return f"200\n{json.dumps(resultado)}"
            else:
                return "404\nNot Found"
        else:
            produto = self.produtos.get(query.lower())
            if produto:
                return f"200\n{json.dumps(produto.dicionario())}"
            else:
                return "404\nNot Found"

    def criar_produto(self, nome, preco):
        nome_formatado = nome.lower()
        if nome_formatado in self.produtos:
            return "409\nConflict"
        try:
            preco = float(preco)
            novo_produto = Produto(nome, preco)
            self.produtos[nome_formatado] = novo_produto
            return f"201\nOK"
        except ValueError:
            return "400\nBad Request"

    def deletar_produto(self, nome):
        nome_formatado = nome.lower()
        if nome_formatado in self.produtos:
            del self.produtos[nome_formatado]
            return f"200\nOK"
        else:
            return "404\nNot Found"

    def processar_requisicao(self, requisicao):
        linhas = requisicao.strip().split("\n")

        if len(linhas) > 0:
            linha_req = linhas[0].split()

            if len(linha_req) >= 2:
                comando = linha_req[0].upper()
                recurso = linha_req[1].strip("/")

                if comando == "SEARCH":
                    return self.consultar_produtos(recurso)
                elif comando == "CREATE" and len(linha_req) == 3:
                    return self.criar_produto(linha_req[1], linha_req[2])
                elif comando == "DELETE":
                    return self.deletar_produto(recurso)
                elif comando == "QUIT":
                    return "200\nOK"

        return "400\nBad Request"

    def handle_client(self, conn, addr):
        try:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                resposta = self.processar_requisicao(data)
                conn.sendall(resposta.encode())
                if data.startswith("QUIT"):
                    break
        except ConnectionError:
            pass
        finally:
            conn.close()


if __name__ == "__main__":
    servidor = Servidor()
    servidor.iniciar()

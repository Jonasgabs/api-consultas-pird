from cliente.cliente import Cliente
import sys


host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
porta = int(sys.argv[2]) if len(sys.argv) > 2 else 8080

cliente = Cliente(host, porta) 

while True:
    consulta = input("Pesquisar (nome ou preço do produto, ou 'SAIR' para sair): ")

    if consulta.upper() == "SAIR":
        cliente.desconectar()
        break

    resposta = cliente.enviar_requisicao(consulta)
    print("Resposta do servidor:", resposta)

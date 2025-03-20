from cliente.cliente import Cliente
import sys
from time import sleep

host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
porta = int(sys.argv[2]) if len(sys.argv) > 2 else 8080

cliente = Cliente(host, porta) 

while True:
    consulta = input("Pesquisar (nome ou preço do produto, ou 'QUIT' para sair): ")

    if consulta.upper() == "QUIT":
        cliente.desconectar()
        break
    
    sleep(0.5)
    resposta = cliente.enviar_requisicao(consulta)
    sleep(0.5)
    print("Resposta do servidor:\n", resposta)
    print("-=" * 50)

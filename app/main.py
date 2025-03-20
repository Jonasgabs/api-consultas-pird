from cliente.cliente import Cliente
import sys
from time import sleep

host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
porta = int(sys.argv[2]) if len(sys.argv) > 2 else 8080

cliente = Cliente(host, porta) 

while True:
    consulta = input("Digite um comando (CREATE, SEARCH, DELETE ou QUIT): ").strip()

    if consulta.upper() == "CREATE":
        nome = input("Nome do produto: ").strip()
        preco = input("Preço do produto: ").strip()

        if not preco.replace(".", "", 1).isdigit():
            print("Erro: Preço inválido.")
            continue

        requisicao = f"CREATE {nome} {preco}"

    elif consulta.upper() == "SEARCH":
        termo = input("Nome ou preço do produto: ").strip()
        requisicao = f"SEARCH {termo}"

    elif consulta.upper() == "DELETE":
        nome = input("Nome do produto a deletar: ").strip()
        requisicao = f"DELETE {nome}"

    elif consulta.upper() == "QUIT":
        cliente.desconectar()
        print("Conexão encerrada.")
        break

    else:
        print("Comando inválido. Use CREATE, SEARCH, DELETE ou QUIT.")
        continue

    sleep(0.5)
    resposta = cliente.enviar_requisicao(requisicao)
    sleep(0.5)
    print("Resposta do servidor:\n", resposta)
    print("-=" * 50)

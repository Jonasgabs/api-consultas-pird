from cliente.cliente import Cliente
import sys
from time import sleep
import json

host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
porta = int(sys.argv[2]) if len(sys.argv) > 2 else 8080

cliente = Cliente(host, porta)

menu = '''
=========================================
  O que você deseja fazer?

  1 → CRIAR   PRODUTO
  2 → BUSCAR  PRODUTO
  3 → DELETAR PRODUTO
  4 → SAIR

=========================================
'''

while True:
    print(menu)
    consulta = input("Escolha uma opção (1-4): ").strip()

    if consulta == "1":
        nome = input("Nome do produto: ").strip()
        preco = input("Preço do produto: ").strip()

        if not preco.replace(".", "", 1).isdigit():
            print("Erro: Preço inválido.")
            continue

        requisicao = f"CREATE {nome} {preco}"

    elif consulta == "2":
        termo = input("Nome ou preço do produto: ").strip()
        requisicao = f"SEARCH {termo}"

    elif consulta == "3":
        nome = input("Nome do produto a deletar: ").strip()
        requisicao = f"DELETE {nome}"

    elif consulta == "4":
        cliente.desconectar()
        print("Conexão encerrada.")
        break

    else:
        print("Opção inválida. Tente novamente.")
        continue

    sleep(0.5)
    resposta = cliente.enviar_requisicao(requisicao)
    sleep(0.5)

    status, *body = resposta.split("\n", 1)
    corpo = body[0] if body else ""

    print("\n=== Resposta do Servidor ===")
    print(f"Status: {status}")

    try:
        json_data = json.loads(corpo)
        if isinstance(json_data, list):
            for i, item in enumerate(json_data, start=1):
                print(f"\nProduto {i}:")
                for chave, valor in item.items():
                    print(f"  {chave.capitalize()}: {valor}")
        elif isinstance(json_data, dict):
            print()
            for chave, valor in json_data.items():
                print(f"{chave.capitalize()}: {valor}")
        else:
            print(f"Mensagem: {json_data}")
    except (json.JSONDecodeError, TypeError):
        if corpo:
            print(f"Mensagem: {corpo}")

    print("=" * 50)

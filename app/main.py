from cliente import Cliente

while True:
    print("Digite o nome ou o preço do produto.")
    consulta = input("Pesquisar: ").upper()

    if consulta == "SAIR":
        ''' Fazer lógica para desconectar o cliente'''
        break

    # resposta = cliente.enviar_requisicao(consulta)
    # print("Resposta do servidor:", resposta)

    # host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    # porta = int(sys.argv[2]) if len(sys.argv) > 2 else 8080 (Pegar IP pelo terminal, implementar)
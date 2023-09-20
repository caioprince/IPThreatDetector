from classes import virusTotal as vt
import os

def analiseIP(opcao,iplist):
    # Obtém o diretório atual do script
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    API_KEY = ''

    # Abre arquivo com a key
    with open(os.path.join(diretorio_atual, '..', 'config', 'config.txt'), 'r') as arquivo:
        # Lê a primeira linha do arquivo
        firstLine = arquivo.readline()
        # Imprime a primeira linha
        API_KEY = firstLine

        if int(opcao) == 1 and "," not in iplist:
            # Coloque aqui a lógica para analisar um único IP
            print(f"\033[92mAnalisando o IP {iplist}...\033[0m")

            virusTotal = vt.verificaIP(API_KEY, iplist).start()
            print(f"\033[91mDetecções de ameaças: {virusTotal}\033[0m")

        elif int(opcao) == 1 and "," in iplist:
            # REALIZA A CONSULTA NO VIRUS TOTAL
            lista_ips = iplist.split(',')
            for ip in lista_ips:
                print(f"\033[92mAnalisando o IP {ip}...\033[0m")
                virusTotal = vt.verificaIP(API_KEY, ip).start()
                print(f"\033[91mDetecções de ameaças: {virusTotal}\033[0m")

def analise():
    # Menu principal
    while True:
        print("\nOpções de Menu:")
        print("1. Digite o IP que deseja analisar ou uma lista separados por virgula: ")
        print("2. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            ip = input("Digite o IP que deseja analisar: ")
            analiseIP(opcao=escolha,iplist=ip)
        elif escolha == '2':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
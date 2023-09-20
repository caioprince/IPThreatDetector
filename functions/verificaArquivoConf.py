import os

def config():
    # Define o caminho para a pasta onde você deseja verificar o arquivo
    pasta = "./config"  # Substitua pelo caminho real da sua pasta

    # Define o caminho completo para o arquivo config.txt
    caminho_arquivo = os.path.join(pasta, "config.txt")

    # Verifica se o arquivo existe
    if os.path.exists(caminho_arquivo):
        return True
    else:
        print("\033[93mA chave do VirusTotal não foi encontrada\033[0m")

        chave = input("Por favor, insira a chave: ")

        # Cria o arquivo e escreve a chave
        with open(caminho_arquivo, "w") as arquivo:
            arquivo.write(chave)
            print("\033[94mA chave foi configurada, vamos prosseguir.\033[0m")

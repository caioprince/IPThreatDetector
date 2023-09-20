
from functions import asciiArt as art, verificaArquivoConf, analiseIp
def main():
    #PRINT DA ARTE DO PROGRAMA
    print(art.asciiArt())
    #VERIFICA A EXISTENCIA DO ARQUIVO
    verificaArquivoConf.config()
    #INICIA O PROCESSO DE DETECCAO
    analiseIp.analise()



if __name__ == '__main__':
    main()




import requests

class conexao:
    def __init__(self, API_KEY, IP_ADDRESS):
        self.API_KEY = API_KEY
        self.IP_ADDRESS = IP_ADDRESS

class verificaIP(conexao):
    def __init__(self,API_KEY,IP_ADDRESS):
        conexao.__init__(self,API_KEY,IP_ADDRESS)

    def start(self):
        # Substitua 'SUA_CHAVE_DE_API' pelo seu próprio valor de chave de API do VirusTotal
        API_KEY = f'{self.API_KEY}'
        IP_ADDRESS = f'{self.IP_ADDRESS}'
        # URL da API do VirusTotal para pesquisa de IP
        url = f'https://www.virustotal.com/api/v3/ip_addresses/{IP_ADDRESS}'

        # Cabeçalho com a chave de API
        headers = {
            'x-apikey': API_KEY
        }

        try:
            # Fazendo a solicitação GET à API do VirusTotal
            response = requests.get(url, headers=headers)

            # Verificando se a solicitação foi bem-sucedida (código de status 200)
            if response.status_code == 200:
                data = response.json()
                qtdAmeaca = data['data']['attributes']['last_analysis_stats']['malicious']


                # Exibindo informações sobre o IP
                #print("Informações sobre o IP:")
                #print(f"IP: {data['data']['id']}")
                #print(f"Detecções de ameaças: {data['data']['attributes']['last_analysis_stats']['malicious']}")
                return qtdAmeaca
            else:
                print(f"Erro na solicitação: {response.status_code} - {response.text}")

        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")


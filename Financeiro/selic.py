import requests

# Função para calcular juros com base na taxa Selic
def calcular_juros(valor_principal, taxa_selic, periodo):
    taxa_juros = taxa_selic / 100
    juros = valor_principal * taxa_juros * periodo
    montante = valor_principal + juros
    return montante

# URL da API do Banco Central do Brasil para obter a taxa Selic
url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json'

try:
    # Faz a requisição GET à API
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Obtém o valor da taxa Selic a partir dos dados retornados
        taxa_selic = float(response.json()[0]['valor'])

        # Solicita ao usuário os dados do cálculo de juros
        valor_principal = float(input('Informe o valor principal: '))
        periodo = int(input('Informe o período em meses: '))

        # Calcula o montante com base na taxa Selic e imprime o resultado
        montante = calcular_juros(valor_principal, taxa_selic, periodo)
        print('O montante após', periodo, 'meses será de R$', montante)
    else:
        # Imprime uma mensagem de erro caso a requisição não tenha sido bem-sucedida
        print('Erro ao obter a taxa Selic. Código de status:', response.status_code)

except requests.exceptions.RequestException as e:
    # Imprime uma mensagem de erro caso ocorra uma exceção na requisição
    print('Erro de requisição:', e)

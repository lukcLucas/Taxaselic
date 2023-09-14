import tkinter as tk
import requests

# Função para calcular juros com base na taxa Selic
def calcular_juros():
    valor_principal = float(principal_entry.get())
    periodo = int(periodo_entry.get())

    # URL da API do Banco Central do Brasil para obter a taxa Selic
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json'

    try:
        # Faz a requisição GET à API
        response = requests.get(url)

        # Verifica se a requisição foi bem-sucedida (código 200)
        if response.status_code == 200:
            # Obtém o valor da taxa Selic a partir dos dados retornados
            taxa_selic = float(response.json()[0]['valor'])

            # Calcula o montante com base na taxa Selic
            montante = valor_principal + (valor_principal * taxa_selic * periodo)

            # Atualiza o resultado na interface
            resultado_label.config(text='O montante após {} meses será de R$ {:.2f}'.format(periodo, montante))
        else:
            resultado_label.config(text='Erro ao obter a taxa Selic. Código de status: {}'.format(response.status_code))

    except requests.exceptions.RequestException as e:
        resultado_label.config(text='Erro de requisição: {}'.format(e))

# Cria a janela da interface
window = tk.Tk()
window.title("Calculadora de Juros")

# Cria os widgets da interface
principal_label = tk.Label(window, text="Valor Principal:")
principal_label.pack()
principal_entry = tk.Entry(window)
principal_entry.pack()

periodo_label = tk.Label(window, text="Período (em meses):")
periodo_label.pack()
periodo_entry = tk.Entry(window)
periodo_entry.pack()

calcular_button = tk.Button(window, text="Calcular", command=calcular_juros)
calcular_button.pack()

resultado_label = tk.Label(window, text="")
resultado_label.pack()

# Inicia o loop da interface
window.mainloop()

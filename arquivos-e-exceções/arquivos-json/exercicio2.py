import json

# Criar
def escrever_json(dados, file_name):
    with open(file_name + '.json', 'w') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False)
        arquivo.close()

dados = "Ola Mundo"
file_name = "arquivos-json/ex2-arquvio-dados"

# escrever_json(dados,file_name)

# Ler
def ler_json(file_name):
    data = {}
    try:
        with open(file_name + '.json', 'r') as arquivo:
            data = json.load(arquivo)
            return data
    except FileNotFoundError:
        

ler_json(file_name)
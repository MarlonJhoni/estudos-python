import json

# Criar
def escrever_json(dados, file_name):
    with open(file_name, 'w') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False)
        arquivo.close()

dados = "Ola Mundo"
file_name = "arquivos-e-excecoes/arquivos-json/ex2-arquvio-dados.json"

escrever_json(dados,file_name)

# Ler
def ler_json(file_name):
    data = {}
    try:
        with open(file_name, 'r') as arquivo:
            data = json.load(arquivo)
            print(data)
    except FileNotFoundError:
            print('Arquivo não encontrado')

ler_json(file_name)


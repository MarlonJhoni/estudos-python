
# Adicionar arquivos no JSON
import json

dados = {
  "nome": "João",
  "idade": 25,
  "cidade": "Curitiba",
  "frutas_favoritas": [
    "maçã",
    "banana",
    "laranja"
  ]
}

# o dicionário dados que será convertido em JSON, a variável arquivo onde os dados serão gravados
# parâmetro ensure_ascii=False para permitir a codificação correta de caracteres não-ASCII (isto é, caracteres que não façam parte do alfabeto da língua inglesa)
with open("arquivos-e-excecoes/arquivos-json/ex1-pessoa.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False)

# Ler arquviso JSON e armazene-o em uma variável chamada dados_lidos
with open("arquivos-e-excecoes/arquivos-json/ex1-pessoa.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)

print(dados_lidos)

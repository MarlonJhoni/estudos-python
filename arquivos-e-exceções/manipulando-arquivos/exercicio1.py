nome = input("Digite seu nome: ")
# "w" arquvio.write() criar um novo arquivo
with open("manipulando-arquivos/dados.txt", "w") as arquivo:
    arquivo.write("Count-Striker é melhor do que Volarant.")
    arquivo.write("O correto é 'bolacha'.")
    arquivo.write(nome)

# "r" ler o conteudo
print("Ler uma linha de cada vez: função readline()")
with open("manipulando-arquivos/dados.txt", "r") as arquivo:
    linhas = arquivo.readline()
    print(linhas)

print("Ler todo o conteúdo do arquivo em uma só string: função read().")
with open("manipulando-arquivos/dados.txt", "r") as arquivo:
    linhas = arquivo.read()
    print(linhas)

print("Ler todo o conteúdo do arquivo separando linha por linha como strings em uma única lista readlines()")
with open("manipulando-arquivos/dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print(linhas)

with open("manipulando-arquivos/dados.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)


primeiro_numero = 1.0
segundo_numero = -2.95

 
# Adicionando dados dentro do arquivo
with open("manipulando-arquivos/dados.txt", "a") as arquivo:

    arquivo.write("\n" + str(primeiro_numero))

    arquivo.write("\n" + str(segundo_numero))


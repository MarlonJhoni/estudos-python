'''
Crie um programa que peça ao usuário cinco números e informe qual é o menor e qual é o maior deles.
'''

maior = 1000000
menor = -1000000

for i in range(5):
    num = int(input("Digite um número: "))
    if num < menor:
        menor = num
    if num < maior:
        maior = num
            
print(f'O maior numero digitado é: {num}')
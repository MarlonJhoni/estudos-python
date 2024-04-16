num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
op = input('Digite a operção matemática: (+ - * /)')
result = 0

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2
else:
    op = 'erro'

if op == 'erro':
    print('Você digitou uma operção inválida')
else:
    print(num1,op,num2,'=',result)

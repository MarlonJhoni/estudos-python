
materia1 = float(input('Digite a nota da primeira matéria: '))
materia2 = float(input('Digite a nota da segunda matéria: '))
materia3 = float(input('Digite a nota da terceira matéria: '))
materia4 = float(input('Digite a nota da quarta matéria: '))
faltas = int(input('Digite o número de faltas: '))

media = (materia1+materia2+materia3+materia4)/4
print(f'Sua média é: {media}')

presenca = 40 * 0.75

if media >= 7 and faltas >= presenca:
    print('Aprovado')
elif media > 7 and faltas < presenca:
    print('Reprovado por falta')
elif media < 7 and faltas > presenca:
    print('Reprovado por nota')
else:
    print('Reprovado por falta e nota')

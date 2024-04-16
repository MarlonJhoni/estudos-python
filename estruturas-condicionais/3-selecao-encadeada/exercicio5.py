
turno = input('Em qual turno você trabalha? (M/T/N)\n'
              'M - Manha\n'
              'T - Tarde\n'
              'N - Noite\n')

if turno == 'M':
    print('Bom dia!')
elif turno == 'T':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Você digitou uma opção inválida.')

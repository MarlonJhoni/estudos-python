# Seleção Composta
salario = float(input('Qual é o seu salário: '))
abono = 0
if salario < 5000:
    # Abono fim de ano de 15%
    abono = salario * 0.15    
else:
    # Abono fim de ano de 10%
    abono = salario * 0.10
    
print(f'O valor do seu abono de fim de ano é {abono}')
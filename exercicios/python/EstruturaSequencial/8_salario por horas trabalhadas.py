valor_por_hora = float(input('Quanto você recebe por horas trabalhadas? '))
horas_trabalhadas = int(input('Quantas horas você trabalhou esse mês? '))

salario_do_mes = valor_por_hora * horas_trabalhadas

print(f'O salário a receber totalizará em R${salario_do_mes} reais.')

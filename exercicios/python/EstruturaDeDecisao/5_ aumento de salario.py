# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario_anterior = float(input("Qual é o seu salário? Digite apenas números: "))

salario_com_ajuste = 0
percentual = ""
aumento = 0

if salario_anterior < 280:
    salario_com_ajuste = salario_anterior * 1.2
    percentual = "20%"
    aumento = salario_com_ajuste - salario_anterior
elif salario_anterior > 280 and salario_anterior <= 700:
    salario_com_ajuste = salario_anterior * 1.15
    percentual = "15%"
    aumento = salario_com_ajuste - salario_anterior
elif salario_anterior > 700 and salario_anterior <= 1500:
    salario_com_ajuste = salario_anterior * 1.1
    percentual = "10%"
    aumento = salario_com_ajuste - salario_anterior
else:
    salario_com_ajuste = salario_anterior * 1.05
    percentual = "5%"
    aumento = salario_com_ajuste - salario_anterior

print(f"""
Salário antes do reajuste: R${salario_anterior:.2f}
Percentual de aumento aplicado: {percentual}
Valor do aumento: R${aumento:.2f}
Salário com o aumento: R${salario_com_ajuste:.2f}
""")

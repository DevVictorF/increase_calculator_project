# Variaveis
salario = float(input("Digite o Salario: "))
aumento = 0
porcentagem = 0
novo_salario = 0.0

#Comparacao
if salario <= 1000.00:
    porcentagem = 20
elif salario >= 1000.01 and salario < 1500.00:
    porcentagem = 15
elif salario >= 1500.01 and salario < 2000.00:
    porcentagem = 10
elif salario >= 2000.01:
    porcentagem = 5

porcentagem = (salario * porcentagem) / 100
novo_salario = salario + porcentagem

# Impressoes dos Resultados
print("Salario anterior: R$ {:.2f}".format(salario))
print("Porcentual de aumento aplicado: {}".format(porcentagem))
print("Valor do aumento: R$ {:.2f}".format(porcentagem))
print("Novo Salario, apos o aumento: R$ {:.2f}".format(novo_salario))
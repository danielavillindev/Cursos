#DESAFIO-30
p1 = float(input("Digite a nota da P1: "))
p2 = float(input("Digite a nota da P2: "))
p3 = float(input("Digite a nota da P3: "))

media = (p1 + p2 + p3) / 3
print(f"A média das notas é: {media:.2f}")

#DESAFIO-31
import math

a = 4
b = 3
hipotenusa = math.sqrt(a**2 + b**2)
print(f"A hipotenusa do triângulo é: {hipotenusa:.2f}")

salario_atual = float(input("Digite o valor do salário atual: "))
percentual_aumento = float(input("Digite o percentual de aumento: "))

aumento = salario_atual * (percentual_aumento / 100)
salario_atualizado = salario_atual + aumento
print(f"O valor do salário atualizado é: {salario_atualizado:.2f}")

#DESAFIO-32
PI = 3.1416
raio = float(input("Digite o raio da lata: "))
altura = float(input("Digite a altura da lata: "))

volume = PI * raio**2 * altura
print(f"O volume da lata de óleo é: {volume:.2f}")

#DESAFIO-33
gols_time1 = int(input("Digite o número de gols do primeiro time: "))
gols_time2 = int(input("Digite o número de gols do segundo time: "))

if gols_time1 > gols_time2:
    print("O primeiro time venceu.")
elif gols_time2 > gols_time1:
    print("O segundo time venceu.")
else:
    print("O jogo empatou.")

#DESAFIO-34
valor_compra = float(input("Digite o valor da compra: "))
numero_prestacoes = int(input("Digite o número de prestações: "))

valor_prestacao = valor_compra / numero_prestacoes
print(f"O valor de cada prestação é: {valor_prestacao:.2f}")


#DESAFIO-35
idade = int(input("Digite a idade do nadador: "))

if 5 <= idade <= 7:
    categoria = "Infantil A"
elif 8 <= idade <= 11:
    categoria = "Infantil B"
elif 12 <= idade <= 13:
    categoria = "Juvenil A"
elif 14 <= idade <= 17:
    categoria = "Juvenil B"
else:
    categoria = "Adultos"

print(f"A categoria do nadador é: {categoria}")

#DESAFIO-36
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print(f"A soma dos números é: {soma:.2f}")
print(f"A subtração dos números é: {subtracao:.2f}")
print(f"A multiplicação dos números é: {multiplicacao:.2f}")
print(f"A divisão dos números é: {divisao:.2f}")

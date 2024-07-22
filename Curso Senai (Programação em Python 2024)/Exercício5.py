#DESAFIO-37
while True:
    sexo = input("Digite o sexo (M/F): ").upper()
    if sexo in ('M', 'F'):
        break
    else:
        print("Sexo inválido! Tente novamente.")
print(f"Sexo {sexo} registrado com sucesso.")


#DESAFIO-38
import random

numero_secreto = random.randint(0, 10)
tentativas = 0

while True:
    palpite = int(input("Adivinhe o número entre 0 e 10: "))
    tentativas += 1
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        break
    else:
        print("Palpite errado. Tente novamente.")


#DESAFIO-39
while True:
    print("\nMenu:")
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos Números")
    print("[5] Sair do programa")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 5:
        break

    if escolha in (1, 2, 3, 4):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

    if escolha == 1:
        print(f"Soma: {num1 + num2}")
    elif escolha == 2:
        print(f"Multiplicação: {num1 * num2}")
    elif escolha == 3:
        maior = num1 if num1 > num2 else num2
        print(f"Maior: {maior}")
    elif escolha == 4:
        continue
    else:
        print("Opção inválida! Tente novamente.")


#DESAFIO-40
num = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

while num > 0:
    fatorial *= num
    num -= 1

print(f"Fatorial: {fatorial}")


#DESAFIO-41
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro_termo
contador = 1

while contador <= 10:
    print(f"{termo} -> ", end="")
    termo += razao
    contador += 1
print("Fim")


#DESAFIO-42
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro_termo
contador = 1
total_termos = 0
mais_termos = 10

while mais_termos != 0:
    total_termos += mais_termos
    while contador <= total_termos:
        print(f"{termo} -> ", end="")
        termo += razao
        contador += 1
    print("Pausa")
    mais_termos = int(input("Quantos termos você quer mostrar a mais? "))
print("Fim")


#DESAFIO-43
n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print(f"{t1} -> {t2} -> ", end="")
contador = 3

while contador <= n:
    t3 = t1 + t2
    print(f"{t3} -> ", end="")
    t1 = t2
    t2 = t3
    contador += 1
print("Fim")


#DESAFIO-44
soma = 0
contador = 0

while True:
    numero = int(input("Digite um número (999 para parar): "))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f"Você digitou {contador} números e a soma entre eles foi {soma}")


#DESAFIO-45
soma = 0
contador = 0
maior = menor = 0

while True:
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = input("Quer continuar? [S/N] ").strip().upper()
    if resposta == 'N':
        break

media = soma / contador
print(f"Você digitou {contador} números e a média foi {media:.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
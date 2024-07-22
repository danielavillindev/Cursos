#DESAFIO-46
soma = 0
contador = 0
while True:
    numero = int(input("Digite um número (999 para parar): "))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f"Você digitou {contador} números e a soma entre eles foi {soma}.")


#DESAFIO-47
while True:
    numero = int(input("Digite um número para ver sua tabuada (número negativo para parar): "))
    if numero < 0:
        break
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


#DESAFIO-48
import random

vitorias = 0

while True:
    jogador = int(input("Diga um valor: "))
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input("Par ou Ímpar? [P/I] ").strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total} ", end='')
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
    if tipo == 'P':
        if total % 2 == 0:
            print("Você VENCEU!")
            vitorias += 1
        else:
            print("Você PERDEU!")
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print("Você VENCEU!")
            vitorias += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {vitorias} vezes.")


#DESAFIO-49
total_mais_18 = total_homens = total_mulheres_menos_20 = 0

while True:
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input("Sexo: [M/F] ").strip().upper()[0]
    if idade > 18:
        total_mais_18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        total_mulheres_menos_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == 'N':
        break

print(f"Total de pessoas com mais de 18 anos: {total_mais_18}")
print(f"Ao todo temos {total_homens} homens cadastrados")
print(f"E temos {total_mulheres_menos_20} mulheres com menos de 20 anos")


#DESAFIO-50
total_gasto = produtos_mais_1000 = 0
produto_mais_barato = ''
preco_produto_mais_barato = float('inf')

while True:
    nome_produto = input("Nome do produto: ")
    preco_produto = float(input("Preço: R$"))
    total_gasto += preco_produto
    if preco_produto > 10000:
        produtos_mais_1000 += 1
    if preco_produto < preco_produto_mais_barato:
        preco_produto_mais_barato = preco_produto
        produto_mais_barato = nome_produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == 'N':
        break

print(f"O total gasto na compra foi R${total_gasto:.2f}")
print(f"Temos {produtos_mais_1000} produtos custando mais de R$10000.00")
print(f"O produto mais barato foi {produto_mais_barato} que custa R${preco_produto_mais_barato:.2f}")


#DESAFIO-51
print("="*30)
print("{:^30}".format("BANCO NUBANK"))
print("="*30)
valor = int(input("Que valor você quer sacar? R$"))
total = valor
cedula = 50
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f"Total de {total_cedulas} cédulas de R${cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0
        if total == 0:
            break
print("="*30)
print("Volte sempre ao BANCO NUBANK! Tenha um bom dia!")

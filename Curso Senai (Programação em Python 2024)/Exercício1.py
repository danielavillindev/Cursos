#DESAFIO-1
media = float(input('informe a nota: '))
if media > 5:
    print('Você foi APROVADO')
else:
    print('Você foi REPROVADO')

#Exercicio em aula


#DESAFIO-2
import random

# O compuatador escolhe um numero aleatório entre 0 e 5
numero_computador = random.randint(0,5)
#solicitar que o usario tente advinhar o numero escolhido pelo computador
tentativa = int(input("Tente advinhar o numero escolhido pelo computador (entre 0 e 5): "))
#verifica se a tentativa do usuario está correta
if tentativa == numero_computador:
    print("Você venceu!")
else:
    print("Você perdeu!")


#DESAFIO-3
#solicita a velocidade do carro ao usuário
velocidade = float(input("Digite a velocidade do carro (km/h): "))
#verifica se a velocidade está acima do limite (80km/h)
if velocidade > 80:
#calcula o valor da multa
    multa = (velocidade - 80) * 7.00
    print(f"Voce foi mutado! A multa é de R$ {multa:.2f}.")
else:
    print(f"Voçê esta dentro do limite de velocidade da via")

#DESAFIO-4
#solicitar um numero inteiro ao usuário
numero = int(input("Digite um numero inteiro: "))
#verificar se o numero é impar ou par
if numero % 2 == 0:
    print(f"O numero {numero} é PAR.")
else:
    print(f"O numero {numero} é IMPAR")

#DESAFIO-5
#solicitar a distância da viagem ao usuário
distância = float(input("Digite a distância da viagem em km: "))
#calcula o preço da passagem com base na distância
if distância == 200:
    preco = distância * 0.50
else:
    preco = distância * 0.45
    print(f"O preço da passagem é R${preco:.2f}")



#DESAFIO-6
def aprovar_emprestimo():
    valor_casa = float(input("Valor da casa: R$ "))
    salario = float(input("Salário do comprador: R$ "))
    anos = int(input("Quantos anos para pagar: "))

    # Calcula o valor da prestação mensal
    prestacao_mensal = valor_casa / (anos * 12)

    # Verifica se a prestação mensal excede 30% do salário
    if prestacao_mensal > (0.3 * salario):
        print("Empréstimo negado.")
    else:
        print("Empréstimo aprovado.")
        print(f"Prestação mensal: R$ {prestacao_mensal:.2f}")


#DESAFIO-7
def conversao_base():
    numero = int(input("Digite um número inteiro: "))
    print("Escolha uma base para conversão:")
    print("1 para Binário")
    print("2 para Octal")
    print("3 para Hexadecimal")
    opcao = int(input("Sua opção: "))

    # Converte o número para a base escolhida
    if opcao == 1:
        print(f"{numero} convertido para Binário é {bin(numero)[2:]}")
    if opcao == 2:
        print(f"{numero} convertido para Octal é {oct(numero)[2:]}")
    if opcao == 3:
        print(f"{numero} convertido para Hexadecimal é {hex(numero)[2:]}")
    if opcao not in (1, 2, 3):
        print("Opção inválida.")


#DESAFIO-8
def comparar_numeros():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # Compara os dois números e mostra a mensagem correspondente
    if num1 > num2:
        print("O primeiro valor é maior.")
    if num2 > num1:
        print("O segundo valor é maior.")
    if num1 == num2:
        print("Não existe valor maior, os dois são iguais.")


#DESAFIO-9
def alistamento_militar():
    from datetime import date
    ano_nascimento = int(input("Ano de nascimento: "))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    # Verifica a situação de alistamento de acordo com a idade
    if idade < 18:
        print(f"Ainda faltam {18 - idade} anos para o alistamento.")
    if idade == 18:
        print("Está na hora de se alistar.")
    if idade > 18:
        print(f"Já passaram {idade - 18} anos do tempo de alistamento.")


#DESAFIO-10
def calcular_media():
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    media = (nota1 + nota2) / 2

    # Calcula a média e mostra a mensagem correspondente
    print(f"Sua média foi {media:.1f}")
    if media < 5.0:
        print("REPROVADO")
    if 5.0 <= media <= 6.9:
        print("RECUPERAÇÃO")
    if media >= 7.0:
        print("APROVADO")


#DESAFIO-11
def categoria_nadador():
    ano_nascimento = int(input("Ano de nascimento: "))
    from datetime import date
    idade = date.today().year - ano_nascimento

    # Determina a categoria do nadador com base na idade
    if idade <= 9:
        categoria = "MIRIM"
    if 9 < idade <= 14:
        categoria = "INFANTIL"
    if 14 < idade <= 19:
        categoria = "JÚNIOR"
    if 19 < idade <= 24:
        categoria = "SÊNIOR"
    if idade > 24:
        categoria = "MASTER"

    print(f"O atleta tem {idade} anos e pertence à categoria {categoria}.")


#DESAFIO-12
def tipo_triangulo():
    lado1 = float(input("Primeiro lado: "))
    lado2 = float(input("Segundo lado: "))
    lado3 = float(input("Terceiro lado: "))

    # Determina o tipo de triângulo com base nos lados
    if lado1 == lado2 == lado3:
        tipo = "Equilátero"
    if lado1 != lado2 != lado3 != lado1:
        tipo = "Escaleno"
    if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        tipo = "Isósceles"

    print(f"Os lados formam um triângulo {tipo}.")

#DESAFIO-13
def calcular_imc():
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    imc = peso / (altura ** 2)

    # Calcula o IMC e mostra o status correspondente
    print(f"Seu IMC é {imc:.1f}")
    if imc < 18.5:
        status = "Abaixo do Peso"
    if 18.5 <= imc < 25:
        status = "Peso Ideal"
    if 25 <= imc < 30:
        status = "Sobrepeso"
    if 30 <= imc < 40:
        status = "Obesidade"
    if imc >= 40:
        status = "Obesidade Mórbida"

    print(f"Status: {status}")


#DESAFIO-14
def calcular_pagamento():
    preco = float(input("Preço do produto: R$ "))
    print("Formas de pagamento:")
    print("[1] à vista dinheiro/cheque")
    print("[2] à vista cartão")
    print("[3] 2x no cartão")
    print("[4] 3x ou mais no cartão")
    opcao = int(input("Qual é a opção? "))

    # Calcula o valor a ser pago de acordo com a forma de pagamento
    if opcao == 1:
        total = preco * 0.9
    if opcao == 2:
        total = preco * 0.95
    if opcao == 3:
        total = preco
    if opcao == 4:
        total = preco * 1.2
    if opcao not in (1, 2, 3, 4):
        total = 0
        print("Opção inválida!")

    print(f"Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f}")


#DESAFIO-15
import random

def jogar_jokenpo():
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = random.randint(0, 2)

    print("Suas opções:")
    print("[0] Pedra")
    print("[1] Papel")
    print("[2] Tesoura")

    jogador = int(input("Qual é a sua jogada? "))

    print(f"Computador jogou {itens[computador]}")
    print(f"Jogador jogou {itens[jogador]}")

    # Determina o resultado do jogo de Jokenpô
    if computador == jogador:
        print("EMPATE")
    if (computador == 0 and jogador == 2) or (computador == 1 and jogador == 0) or (computador == 2 and jogador == 1):
        print("COMPUTADOR VENCE")
    if (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
        print("JOGADOR VENCE")


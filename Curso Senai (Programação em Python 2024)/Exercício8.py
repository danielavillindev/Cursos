#DESAFIO-57
#Tupla com números por extenso
numeros_por_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
    'dezoito', 'dezenove', 'vinte'
)

#Solicita um número do usuário
numero = int(input("Digite um número entre 0 e 20: "))

#Valida se o número está no intervalo correto e mostra por extenso
if 0 <= numero <= 20:
    print(f"Você digitou o número {numeros_por_extenso[numero]}.")
else:
    print("Número fora do intervalo permitido.")


#DESAFIO-58
#Tupla com os 20 primeiros colocados da Série B (exemplo)
times_serie_b = (
    'Botafogo-SP', 'Criciúma', 'Vitória', 'Sport', 'Guarani',
    'Juventude', 'Novorizontino', 'Atlético-GO', 'Londrina', 'CRB',
    'Ponte Preta', 'Chapecoense', 'Sampaio Corrêa', 'Vila Nova',
    'ABC', 'Avaí', 'Ituano', 'Ceará', 'Tombense', 'Mirassol'
)

#Mostra os 5 primeiros colocados
print("Os 5 primeiros colocados são:")
print(times_serie_b[:5])

# Mostra os 4 últimos colocados
print("\nOs 4 últimos colocados são:")
print(times_serie_b[-4:])
#Mostra os times em ordem alfabética

print("\nTimes em ordem alfabética:")
print(sorted(times_serie_b))

#Posição do Santos (se estivesse na Série B)
time_santos = "Santos"
if time_santos in times_serie_b:
    print(f"\nO Santos está na posição {times_serie_b.index(time_santos) + 1}.")
else:
    print(f"\nO Santos não está na Série B.")


#DESAFIO-59
import random

#Gera cinco números aleatórios e armazena em uma tupla
numeros = (
    random.randint(1, 100), random.randint(1, 100),
    random.randint(1, 100), random.randint(1, 100),
    random.randint(1, 100)
)

#Mostra a listagem de números gerados
print("Os números gerados são:")
print(numeros)

#Indica o menor e o maior valor
print(f"O menor valor é {min(numeros)}.")
print(f"O maior valor é {max(numeros)}.")


#DESAFIO-60
#Lê quatro valores pelo teclado e guarda em uma tupla
valores = (
    int(input("Digite o primeiro valor: ")),
    int(input("Digite o segundo valor: ")),
    int(input("Digite o terceiro valor: ")),
    int(input("Digite o quarto valor: "))
)

#mostra quantas vezes apareceu o valor 9
print(f"O valor 9 apareceu {valores.count(9)} vezes.")

#Mostra a posição do primeiro valor 3 (se existir)
if 3 in valores:
    print(f"O valor 3 apareceu pela primeira vez na posição {valores.index(3) + 1}.")
else:
    print("O valor 3 não foi digitado.")

#Mostra os números pares
print("Os números pares são:")
for valor in valores:
    if valor % 2 == 0:
        print(valor, end=' ')


#DESAFIO-61
#Tupla com nomes de produtos e seus respectivos preços
produtos = (
    'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
    'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
    'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90
)

#Mostra a listagem de preços de forma tabular
print("Listagem de preços:")
print("-" * 30)
for i in range(0, len(produtos), 2):
    print(f"{produtos[i]:.<20} R$ {produtos[i+1]:>7.2f}")
print("-" * 30)


#DESAFIO-62
# Tupla com várias palavras
palavras = (
    'aprender', 'programar', 'linguagem', 'python',
    'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
    'mercado', 'programador', 'futuro'
)

# Mostra as vogais de cada palavra
for palavra in palavras:
    print(f"\nNa palavra {palavra.upper()} temos as vogais: ", end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')

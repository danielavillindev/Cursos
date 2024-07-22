#DESAFIO-20
for i in range (1, 51):
    if i % 2 == 0:
        print(i)

soma = 0
for i in range (1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma +=i
        print("A soma de todos os numero impares multiplos de tres entre 1 e 500 é: ", soma)

#DESAFIO-21
num = int(input("Digite um numero para ver a sua tabuada: "))
for i in range (1, 11):
    print(f"{num} x {i} = {num * i}")

pares = []
for _ in range(2):
    num = int(input("Digite um numero um inteiro: "))
    if num % 2 == 0:
        pares.append(num)
        print("A soma dos numeros pares é:", sum(pares))

#DESAFIO-22
primeiro = int(input("Primeiro termo da PA: "))
razao = int(input("Razão do PA: "))
for i in range(10):
    primeiro = primeiro + razao
    print(primeiro)

#DESAFIO-23
numero = int(input("Digite um numero inteiro: "))
eh_primo = True
if numero < 2:
    eh_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
        if eh_primo:
            print(f"O numero {numero} é primo.")
        else:
            print(f"O numero {numero} não é primo.")

#DESAFIO-24
frase = input("Digite uma frase: ").replace(" ", " ").lower()
eh_palindromo = frase == frase [ : : -1]
print(f"A frase {'é' if eh_palindromo else 'não é'} um palindromo.")

#DESAFIO-25
from datetime import datetime
ano_atual = datetime.now().year
maiores = 0
menores = 0
for _ in range(7):
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

    print(f"Maiores de idade: {maiores}")
    print(f"Menores de idade: {menores}")

#DESAFIO-26
pesos = []
for _ in range(5):
    peso = float(input("Digite o peso: "))
    pesos.append(peso)

    print(f"O maior peso é: {max(pesos)} kg")
    print(f"O menor peso é: {min(pesos)} kg")


#DESAFIO-27
pessoas = []
idades = []
sexos = []
mulheres_menores_20 = 0
homem_mais_velhos = (" ", 0)
for _ in range(2):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F)").upper()
    pessoas.append(nome)
    sexos.append(sexo)
    idades.append(idade)
    if sexo == 'M' and idade > homem_mais_velhos[1]:
        homem_mais_velhos = (nome, idade)
    if sexo == 'F' and idade < 20:
        mulheres_menores_20 += 1
media_idade = sum(idades) / 4
print(f"A media de idade do grupo é: {media_idade}")
print(f"O nome do homem mais velho é: {homem_mais_velhos[0]}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menores_20}")


#DESAFIO-28
sexo= []
while sexo not in ("M", "F"):
    sexo = input("Digite o sexo (M/F): ").upper()
    print(f"Entrada invalida, TENTE NOVAMENTE")
sexo = input("Digite o sexo (M/F): ").upper()
print(f"sexo informado corretamente:{sexo}")

#DESAFIO-29
import random
numero_secreto=random.randint(0, 10)
palpite=None
tentativa=0
print("Tente advinhar o numero que eu estou pensando entre 0 a 10")
while palpite != numero_secreto:
#DESAFIO-63

import random

jogadores = {}
for i in range(5):
    jogadores [f"jogador {i}"] = random.randint(1, 6)

jogadores_ordenados = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))

print((jogadores_ordenados))


#DESAFIO-64
pessoas = {}
while True:
    nome = input("Digite o nome da pessoa (ou sair para encerrar): ")
    if nome.lower() == "sair":
        break
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ctps = int(input("Digite a carteira de trabalho (0 se nao tiver): "))

    pessoa = {
        "idade": 2024 - ano_nascimento
    }

    if ctps != 0:
        pessoa["ctps"] = ctps
        pessoa["ano_contratação"] = int(input("Digite o ano de contração: "))
        pessoa["salario"] = float(input("Digite o salário: "))
        pessoa["aposentadoria"] = pessoa["idade"] + (35 - (2024 - pessoa["ano_contratação"]))

    pessoas[nome] = pessoa
print(pessoas)


#DESAFIO-65
jogador = {}
jogador["nome"] = input("Digite o nome do jogador: ")
jogador["partidas"] = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))

gols = []
for i in range(1, jogador["partidas"] + 1):
    gols.append(int(input(f"Quantos gols na partida {i}?")))

jogador["gols"] = gols
jogador["total"] = sum(gols)
print(jogador)


#DSAFIO-66
pessoas = []
while True:
    nome = input("Digite o nome da pessoa ( ou sair para encerrar): ")
    if nome.lower() == "sair":
        break
    sexo = input("Digite o sexo da pessoa (M/F): ")
    idade = int(input("Digite a idade da pessoa: "))

    pessoa = {
        "nome": nome,
        "sexo": sexo,
        "idade": idade
    }
    pessoas.append(pessoa)
quantidade = len(pessoas)
media_idade = sum([p["idade"] for p in pessoas]) / quantidade
mulheres = [p["nome"]for p in pessoas if p["sexo"].lower() == "f"]
acima_da_media = [p["nome"] for p in pessoas if p["idade"] > media_idade]

print(f"Quantidade de pessoas cadastradas: {quantidade}")
print(f"Media de idade do grupo: {media_idade:.2f}")
print(f"lista de mulheres: {mulheres}")
print(f"Lista de mulheres com idade acima da media: {acima_da_media}")


#DESAFIO-67
jogadores = []

while True:
    jogador = {}
    jogador["nome"] = input("Digite o nome do jogador ou (sair pra encerra): ")
    if jogador["nome"].lower() == "sair":
        break
    jogador["partidas"] = int(input(f"Quantas partidas {jogador["nome"]} Jogou?"))

    gols = []
    for i in range(1, jogador["partidas"] + 1):
        gols.append(int(input(f"Quantos gols na partida {i}")))

    jogador["gols"] = gols
    jogador["total"] = sum(gols)
    jogadores.append(jogador)

for j in jogadores:
    print(f"\nJogador:{j["nome"]}")
    print(f"Total de gols:{j["total"]}")
for i, g in enumerate(j["gols"]):
    print(f"Partida {i + 1}: {g} gols")
















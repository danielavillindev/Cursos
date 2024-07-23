#DESAFIO-52
valores = []
for i in range(5):
    valores.append(int(input("digite o valor:")))
maior=max(valores)
menor=min(valores)
pos_maior= valores.index(maior)
pos_menor= valores.index(menor)

print(f"O maior valor é {maior} na posição {pos_maior}")
print(f"O menor valor é {menor} na posição {pos_menor}")

#DESAFIO-53
valores =[]
while True:
    valor =int(input("Digite um valor(ou 999 para sair):"))
    if valor == 999:
        break
    if valor not in valores:
        valores.append(valor)
valores.sort()
print(f"Valores Unicos digitados em ordem crescente:",valores)

#DESAFIO-54
valores = []
while True:
    valor = int(input("Digite um valor (ou 999 para sair):"))
    if valor == 999:
        break
    valores.append(valor)
qnt = len(valores)
valores.sort(reverse=True)
conta_cinco = 5 in valores
print(f"quantidade de valores digitados:{qnt}")
print(f"Lista de valores em ordem decrescente:{valores}")
print(f"O valor 5 {"foi" if conta_cinco else "não foi"} digitado e {"esta" if conta_cinco else "não esta"} na lista")

#DESAFIO-55
num = []
pares = []
impar = []
while True:
    numero = int (input("Digite um valor (ou 999 para sair):"))
    if numero == 999:
        break
    num.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impar.append(numero)
print(f"lista completa:{num}")
print(f"lista de pares:{pares}")
print(f"lista de impares:{impar}")

#DESAFIO-56
import random

lista1 = ["Flamengo", "Palmeiras", "São Paulo", "Athletico-PR", "Atlético-MG", "Corinthians", "Fluminense", "Grêmio", "Fortaleza", "Internacional", "Bahia", "Botafogo", "Red Bull Bragantino", "Atlético-GO", "Ceará", "Cuiabá"]
lista2 = ["Goiás", "Vasco", "Juventude", "Sport", "CRB", "Vitória", "Criciúma", "Sampaio Corrêa", "Operário-PR", "Botafogo-SP", "Brusque", "Ypiranga-RS", "América-RN", "Amazonas", "Águia de Marabá", "Sousa-PB"]

times = lista1 + lista2
random.shuffle(times)

# Sorteio dos jogos
jogos = []
for i in range(len(times)):
    for j in range(i+1, len(times)):
        jogos.append((times[i], times[j]))

# Simulação dos jogos
resultados = {}
for time in times:
    resultados[time] = 0

for jogo in jogos:
    gols_time1 = random.randint(0, 5)
    gols_time2 = random.randint(0, 5)
    if gols_time1 == gols_time2:
        resultados[jogo[0]] += 1
        resultados[jogo[1]] += 1
    elif gols_time1 > gols_time2:
        resultados[jogo[0]] += 3
    else:
        resultados[jogo[1]] += 3

# Listar os classificados por turno
classificacao = sorted(resultados.items(), key=lambda item: item[1], reverse=True)
print("Classificação final:")
for time, pontos in classificacao:
    print(f"{time}: {pontos} pontos")

# Selecionar os 8 primeiros times classificados
classificados = [time for time, pontos in classificacao[:8]]

# Fase de mata-mata
print("\nQuartas de final:")
quartas = [(classificados[i], classificados[i+1]) for i in range(0, len(classificados), 2)]
vencedores_quartas = []
for jogo in quartas:
    gols_time1 = random.randint(0, 5)
    gols_time2 = random.randint(0, 5)
    vencedor = jogo[0] if gols_time1 > gols_time2 else jogo[1]
    vencedores_quartas.append(vencedor)
    print(f"{jogo[0]} {gols_time1} vs {jogo[1]} {gols_time2} -> Vencedor: {vencedor}")

print("\nSemifinais:")
semifinais = [(vencedores_quartas[i], vencedores_quartas[i+1]) for i in range(0, len(vencedores_quartas), 2)]
vencedores_semifinais = []
for jogo in semifinais:
    gols_time1 = random.randint(0, 5)
    gols_time2 = random.randint(0, 5)
    vencedor = jogo[0] if gols_time1 > gols_time2 else jogo[1]
    vencedores_semifinais.append(vencedor)
    print(f"{jogo[0]} {gols_time1} vs {jogo[1]} {gols_time2} -> Vencedor: {vencedor}")

print("\nFinal:")
gols_time1 = random.randint(0, 5)
gols_time2 = random.randint(0, 5)
final = (vencedores_semifinais[0], vencedores_semifinais[1])
campeao_copa_brasil = final[0] if gols_time1 > gols_time2 else final[1]
print(f"{final[0]} {gols_time1} vs {final[1]} {gols_time2} -> Campeão: {campeao_copa_brasil}")

print(f"\nO campeão da Copa do Brasil é: {campeao_copa_brasil}")
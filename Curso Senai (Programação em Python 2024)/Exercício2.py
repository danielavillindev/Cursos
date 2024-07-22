#DESAFIO-16
cidade = input("Digite o nome de uma cidade: ").strip()
if cidade[:5].lower() == "santo":
    print("Sim, a cidade começa com 'Santo'.")
else:
    print("Não, a cidade não começa com 'Santo'.")

#DESAFIO-17
nome = input("Digite o nome de uma pessoa: ").strip()
if "silva" in nome.lower():
    print("Sim, a pessoa tem 'Silva' no nome.")
else:
    print("Não, a pessoa não tem 'Silva' no nome.")

#DESAFIO-18
frase = input("Digite uma frase: ").strip().lower()
letra = 'a'
contagem = frase.count(letra)
primeira_posicao = frase.find(letra) + 1
ultima_posicao = frase.rfind(letra) + 1

print(f"A letra '{letra.upper()}' aparece {contagem} vezes.")
print(f"A primeira posição em que aparece é {primeira_posicao}.")
print(f"A última posição em que aparece é {ultima_posicao}.")


#DESAFIO-19
nome_completo = input("Digite o nome completo de uma pessoa: ").strip()
nomes = nome_completo.split()

primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

print(f"Primeiro: {primeiro_nome}")
print(f"Último: {ultimo_nome}")


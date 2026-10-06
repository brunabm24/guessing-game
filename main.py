import random

class Config:
    def __init__(self, nome, nivel, tentativas):
        self.nome = nome
        self.nivel = nivel
        self.tentativas = tentativas

print("\nWelcome to the Guessing Game!")
while True:

    nomeInput = input("Digite seu nome: ")

    nivelInput = int(input("Escolha o seu nivel de nivel " \
    "\n1 - Fácil (15 tentativas) " \
    "\n2 - Médio (10 tentativas) " \
    "\n3 - Difícil (5 tentativas) " \
    "\n4 - Impossível (3 tentativas) " \
    "\n\nPressione Enter para continuar..."))

    if nivelInput !=    int(1) and nivelInput != int(2) and nivelInput != int(3) and nivelInput != int(4):
        print("\nOpção inválida! Por favor, selecione um nível de nivel válido.")
        continue

    else:
        break

def get_tentativas(nivel):
    if nivel == 1:
        return 15
    elif nivel == 2:
        return 10
    elif nivel == 3:
        return 5
    elif nivel == 4:
        return 3


nivel = nivelInput
nome = nomeInput.capitalize().strip()
tentativas = get_tentativas(nivel)


while True:
    secret_number = random.randint(1, 100)
    tries = tentativas
    previous_guesses = []
    lower_limit = 1
    upper_limit = 100

    print(f"\nBem-vindo ao jogo de adivinhação, {nome}! Adivinhe o número secreto de 1 a 100. Você tem {tries} tentativas!")

    while tries > 0:
        print(f"\nVocê tem {tries} tentativas restantes.")

        if previous_guesses:
            print(f"Palpites anteriores: {previous_guesses}")
            print(f"Intervalo atual: {lower_limit} a {upper_limit}")

        prediction = input("\nDigite seu palpite: ")

        try:
            prediction = int(prediction)
        except ValueError:
            print("\nEntrada inválida! Por favor, digite um número inteiro.")
            continue

        if prediction < lower_limit or prediction > upper_limit:
            print(f"\nPalpite fora do intervalo! Por favor, digite um número entre {lower_limit} e {upper_limit}.")
            continue

        previous_guesses.append(prediction)

        if prediction < secret_number:
            print("Muito baixo!")
            lower_limit = max(lower_limit, prediction + 1)
        elif prediction > secret_number:
            print("Muito alto!")
            upper_limit = min(upper_limit, prediction - 1)
        else:
            print(f"\nParabéns, {nome}! Você acertou o número secreto {secret_number}!")
            replay = input("\nQuer tentar a sorte mais uma vez? Pressione 1 para jogar novamente ou qualquer outra tecla para sair: ")
            if replay == "1":
                break
            else:
                exit()

        tries -= 1

    if tries == 0:
        print(f"\nSuas tentativas acabaram! O número secreto era {secret_number}.")

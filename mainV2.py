import random


class GuessingGame:

    DIFFICULTIES = {
        1: ("Fácil", 15),
        2: ("Médio", 10),
        3: ("Difícil", 5),
        4: ("Impossível", 3),
    }

    def __init__(self, player_name: str, difficulty_choice: int):
        self.player_name = player_name.strip().capitalize()
        self.difficulty_name, self.tries = self.DIFFICULTIES.get(
            difficulty_choice, ("Médio", 10)
        )
        self.secret_number = random.randint(1, 100)
        self.lower_limit = 1
        self.upper_limit = 100
        self.previous_guesses = []

    def make_guess(self, guess: int) -> str:
        """Processa a tentativa do jogador e atualiza os limites dinâmicos."""
        if guess in self.previous_guesses:
            return "DUPLICATE"

        self.previous_guesses.append(guess)
        self.tries -= 1

        if guess == self.secret_number:
            return "WIN"
        elif guess < self.secret_number:
            self.lower_limit = max(self.lower_limit, guess + 1)
            return "LOW"
        else:
            self.upper_bound = min(self.upper_limit, guess - 1)
            return "HIGH"


def run_game():
    print("=== Welcome to the Guessing Game! ===")
    name = input("Digite seu nome: ")

    print(
        "\nEscolha o nível de dificuldade:\n"
        "1 - Fácil (15 tentativas)\n"
        "2 - Médio (10 tentativas)\n"
        "3 - Difícil (5 tentativas)\n"
        "4 - Impossível (3 tentativas)"
    )

    while True:
        try:
            level = int(input("\nOpção (1-4): "))
            if level in [1, 2, 3, 4]:
                break
            print("Por favor, selecione uma opção entre 1 e 4.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

    # Instancia a classe com o estado do jogo
    game = GuessingGame(name, level)

    print(
        f"\nBem-vindo, {game.player_name}! Você escolheu a dificuldade {game.difficulty_name} ({game.tries} tentativas)."
    )

    while game.tries > 0:
        print(
            f"\nTentativas restantes: {game.tries} | Intervalo: {game.lower_limit} a {game.upper_limit}"
        )
        if game.previous_guesses:
            print(f"Palpites anteriores: {game.previous_guesses}")

        try:
            guess = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue

        result = game.make_guess(guess)

        if result == "DUPLICATE":
            print("Você já tentou esse número! Tente outro sem perder tentativa.")
        elif result == "WIN":
            print(
                f"\nParabéns, {game.player_name}! Você acertou o número {game.secret_number}!"
            )
            return
        elif result == "LOW":
            print("Muito baixo!")
        elif result == "HIGH":
            print("Muito alto!")

    print(f"\nSuas tentativas acabaram! O número secreto era {game.secret_number}.")


if __name__ == "__main__":
    run_game()
import random

# Opções do jogo
opcoes = ["pedra", "papel", "tesoura"]

# Função para determinar o vencedor
def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        return "Você venceu!"
    else:
        return "O computador venceu!"

# Loop principal do jogo
while True:
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    
    escolha_jogador = int(input("Digite o número correspondente à sua escolha: ")) - 1
    
    if escolha_jogador not in [0, 1, 2]:
        print("Escolha inválida! Tente novamente.")
        continue
    
    jogador = opcoes[escolha_jogador]
    computador = random.choice(opcoes)
    
    print(f"\nVocê escolheu: {jogador}")
    print(f"O computador escolheu: {computador}\n")
    
    print(determinar_vencedor(jogador, computador))
    
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar!")
        break
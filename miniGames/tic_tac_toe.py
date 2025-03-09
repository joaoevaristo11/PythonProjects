import random
import time
import keyboard

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

def mostrar_tabuleiro(tab):
    posicoes = [[str(i + j * 3 + 1) if tab[j][i] == " " else tab[j][i] for i in range(3)] for j in range(3)]
    for linha in posicoes:
        print(" | ".join(linha))
        print("-" * 9)

def menu():
    print("-------------------------------------\n ❤️  WELCOME TO TICTACTOE GAME ❤️ \n-------------------------------------")
    print("No inicio do jogo vai ser lançado um dado\nO maior valor que sair é quem começa.")
    for i in range(5, 0, -1):
        print(f"O jogo vai começar em {i}...", end="\r")
        time.sleep(1)
    print("\n\nVamos jogar!          \n\n")

def roll_the_dice():
    print("Pressiona 'SPACE' para lançar o dado...")    
    keyboard.wait("space")

    while True:
        your_dice = random.randint(1, 6)
        computer_dice = random.randint(1, 6)

        print("\nO teu dado:")
        for line in dice_art[your_dice]:
            print(line)

        time.sleep(1)

        print("\nDado do computador:")
        time.sleep(2)
        for line in dice_art[computer_dice]:
            print(line)

        if your_dice != computer_dice:
            break
        print("\nEmpate! Vamos lançar de novo...\n")
        time.sleep(1)

    if your_dice > computer_dice:
        print("\n🎉 Tu começas! 🎉\n")
        return "X"
    else:
        print("\n🤖 O computador começa! 🤖\n")
        return "O"

def victory(tab, player):
    for linha in range(3):
        if tab[linha][0] == tab[linha][1] == tab[linha][2] == player:
            return True
    for coluna in range(3):
        if tab[0][coluna] == tab[1][coluna] == tab[2][coluna] == player:
            return True
    if tab[0][0] == tab[1][1] == tab[2][2] == player:
        return True
    if tab[0][2] == tab[1][1] == tab[2][0] == player:
        return True
    return False

def verificar_empate(tab):
    for linha in tab:
        if " " in linha:
            return False
    return True

def inverterJogador(jogadorAtual):
    return "O" if jogadorAtual == "X" else "X"

def jogo():
    jogador_atual = roll_the_dice()
    while True:
        mostrar_tabuleiro(tabuleiro)
        
        if jogador_atual == "X":
            print("\nTua vez!")
            while True:
                try:
                    escolha = int(input("Escolha uma posição (1-9): ")) - 1
                    linha, coluna = escolha // 3, escolha % 3
                    if tabuleiro[linha][coluna] != " ":
                        print("Posição já ocupada! Tenta novamente.")
                    else:
                        tabuleiro[linha][coluna] = "X"
                        break
                except (ValueError, IndexError):
                    print("Entrada inválida! Escolhe um número entre 1 e 9.")
        else:
            print("\nVez do computador...")
            time.sleep(1)
            while True:
                escolha = random.randint(0, 8)
                linha, coluna = escolha // 3, escolha % 3
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = "O"
                    break
        
        if victory(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f"🎉 {'Tu venceste!' if jogador_atual == 'X' else 'O Computador venceu!'} 🎉")
            break
        elif verificar_empate(tabuleiro):
            print("🤝 Empate! 🤝")
            break
        
        jogador_atual = inverterJogador(jogador_atual)

def main():
    menu()
    jogo()
  
main()
 
import random

options = ["Rock", "Paper", "Scissors"]

def oponent():
    return options[random.randint(0, 2)]

def myTurn():
    while True:
        try:
            option = int(input("1. Rock\n2. Paper\n3. Scissors\n\nEscolha uma opção (1, 2 ou 3): "))
            if option in [1, 2, 3]:
                return options[option - 1]
            else:
                print("Opção inválida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

mypoints = 0
oponentPoints = 0

print("\n🪨📄✂️ Bem-vindo ao Jogo Pedra, Papel, Tesoura! ✂️📄🪨\n")

while mypoints < 3 and oponentPoints < 3:
    myChoice = myTurn()
    oponentChoice = oponent()
    
    print(f"\nVocê escolheu: {myChoice}")
    print(f"O oponente escolheu: {oponentChoice}")
    
    if(myChoice==oponentChoice): 
        print("Empate...")
    elif(myChoice == "Rock" and oponentChoice == "Scissors") or \
        (myChoice == "Paper" and oponentChoice == "Rock") or \
        (myChoice == "Scissors" and oponentChoice == "Paper"):
            print("YOU WON this round !!!")
            mypoints+=1
    else:
        print("You Lost this round ...")
        oponentPoints+=1
    print(f"\nPontuação: Você: {mypoints} - Oponente: {oponentPoints}\n")

if mypoints == 3:
    print("🎉 PARABÉNS! Você venceu o jogo! 🎉")
else:
    print("😢 O oponente venceu. Boa sorte na próxima vez!")

print("\nObrigado por jogar! 👋")
    

    
    
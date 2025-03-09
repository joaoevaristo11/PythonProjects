import random

def guessingNumber(min,max):
    number=random.randint(min,max)
    i=0
    
    while(i<3):
        guess = int(input(f"\nEscolha um número entre {min} e {max}: "))
        if(guess==number):
            print("CORRETISSIMO!!!")
            break
        else:
            print("Nada disso... tente novamente")
        
        i+=1
        

print("-------------------------\nBem vindo ao Number Guessing Game\n-------------------------\n")
min=int(input("Define o número mais baixo: "))
max=int(input("Define o número mais alto: "))

guessingNumber(min,max)

print("\n\nEspero que tenha gostado, até à próxima")

"""# Python number guessing game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")"""
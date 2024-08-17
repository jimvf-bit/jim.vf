import os
import random

os.system("clear")

def clear():
    os.system("clear")
    
def game():
    input("Think of a number between 1 and 10 and press any key. I will guess it🧐: ")

    guessed_number = random.randint(1, 10)
    guess = input(f"You thought of the number {guessed_number}:\nCorrect (c), the number I guessed is larger (+), or smaller (-): ") 
    
    guess_count1 = 0

    while True:
        guess_count1 += 1
    
        if guess == '+':
            guessed_number += random.randint(1, 10)
            
        elif guess == '-':
            guessed_number -= random.randint(1, 10)
            
        elif guess == 'c':
            clear()
            print(f"\nI guessed it in {guess_count1} tries!")
            break    
        
        print(f"You thought of the number {guessed_number}:\nCorrect (c), the number I guessed is larger (+), or smaller (-): ", end = '')
    
      
    guess_count = 0
    guessed_number = random.randint(1, 10)
    print("\nI thought of a number between 1 and 10. Can you guess it?\n>>> ")

    while True:
        guess_count += 1
        guess = int(input())
        if guess == guessed_number:
            print(f"You guessed it in {guess_count} tries!")
            break
        elif guess < guessed_number:
            print("Guess a larger number:\n>>> ", end = '')
            
        else:
            print("Guess a smaller number:\n>>> ", end = '')
    
    if guess_count1 == guess_count:
      print(f"Score {guess_count}-{guess_count1}\nIt's a draw😏")
    elif guess_count1 > guess_count:
      print(f"Score {guess_count}-{guess_count1}\nYou win😭")  
    else:
      print(f"Score {guess_count1}-{guess_count}\nI win🥳")
      
    repeat = input("\nWould you like to play again? y/n: ")
    if repeat == 'y':
        clear()
        print("Let's play the number guessing game!")
        game()
    else:
        print("Thank you for playing😊")
 
game()

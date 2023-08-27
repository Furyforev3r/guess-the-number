import random

def Game():
    numbermax = input("Please enter a number: ")
    try:
        number = random.randint(1, int(numbermax))
    except ValueError as err:
        print(f"Please enter a number! ({err})")
        Game()
    inputNumber = 0
    while inputNumber != number:
        try:
            inputNumber = int(input(f"Please enter a number between 1 and {numbermax}: "))
        except ValueError as err:
            print(f"Please enter a number between 1 and {numbermax}! ({err})")
            Game()
        if inputNumber == number:
            break
        elif inputNumber < number:
            print("Too low")
        elif inputNumber > number:
            print("Too high")
    print("You guessed it!")
    finish = input("Would you like to play again? (y/n) ")
    if finish == "y":
        Game()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    Game()

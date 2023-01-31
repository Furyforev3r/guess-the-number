import random #importing random module

def Game(): #defining a function called Game
    numbermax = input("Please enter a number: ") #prompting user to enter a number
    try:
        number = random.randint(1, int(numbermax)) #using random module to generate a random number between 1 and the number entered by the user
    except ValueError as err:
        print(f"Please enter a number! ({err})") #if the number entered by the user is not a number, print this message
        Game() #calling the function again
    inputNumber = 0
    while inputNumber != number: #while the inputNumber is not equal to the number entered by the user
        try:
            inputNumber = int(input(f"Please enter a number between 1 and {numbermax}: ")) #prompting user to enter a number between 1 and the number entered by the user
        except ValueError as err:
            print(f"Please enter a number between 1 and {numbermax}! ({err})") #if the number entered by the user is not a number, print this message
            Game() #calling the function again
        if inputNumber == number:
            break #if the inputNumber is equal to the number entered by the user, break the loop
        elif inputNumber < number:
            print("Too low") #if the inputNumber is less than the number entered by the user, print this message
        elif inputNumber > number:
            print("Too high") #if the inputNumber is greater than the number entered by the user, print this message
    print("You guessed it!") #if the inputNumber is equal to the number entered by the user, print this message
    finish = input("Would you like to play again? (y/n) ") #prompting user to enter a y or n
    if finish == "y":
        Game() #calling the function again
    else:
        print("Goodbye!") #if the user does not want to play again, print this message
Game() #calling the function to start the game
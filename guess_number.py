number = 10
chances = 5
while chances > 0:
    print("I'm thinking of a number...")
    guess = (input(f"What number am I thinking of? You have {chances} chances left: "))

    if guess == 'q':
        print(f"Sorry! The number was {number}.")
        break
    guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess > number:
        print('Sorry! The number was lower ')
    elif guess < number:
        print('Sorry! The number was higher ')
    
    else:
        print(f"Sorry! Please Try Again")
    chances -= 1
else:
    print(f"Sorry, you've run out of guesses. The number was {number}.")

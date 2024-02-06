number = 10
while True:
    print("I'm thinking of a number...")
    guess = (input("What number am I thinking of? "))

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess == 'q':
        print(f"Sorry! The number was {number}.")
        break
    else:
        print(f"Sorry! Please Try Again")

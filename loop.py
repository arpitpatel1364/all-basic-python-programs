secret_number = 77
while True:
    user_guess = int(input("Guess a number between 1 and 100: "))
    if user_guess == secret_number:
        print(" Congratulations! You guessed the correct number.")
        break
    else:
        print("Try again!")
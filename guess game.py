def guess_game():
    i = 0
    num = 9
    while i < 3:
        guess = int(input("Guess: "))
        i += 1

        if guess == num:
            print("You won!")
            exit()
    else:
        print("Sorry you failed!")


guess_game()

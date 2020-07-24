# Guessing game in python , up to 4 players can play


def guessing_game():         # define a function
    import random            # import random module for program to create a random number

    secret_number = random.randint(1, 20)   # this will create a random number in the given range
    chances = 0        # declare a variable

    while chances < 10:  # if a player takes more than 10 chances the game will over
        try:      # we will use try and except block so that program would not stop at any error
            chances = chances + 1  # this will increment the chances on each turn
            print("guess number :- " + str(chances))  # it will print the user chance
            guess = int(input("Enter a number:\n"))   # number input from the user

            if guess > secret_number:  # condition
                print("your number is greater than the secret number")
                if chances == 10:
                    print("sorry you are out of guesses")

            elif guess < secret_number:
                print("your number is lesser than the secret number")
                if chances == 10:
                    print("sorry you are out of guesses")

            else:
                print("congratulations you have guessed the secret number " + str(secret_number) +
                      " in " + str(chances) + " guesses.")   # it will display the secret number and guesses
                break        # this will break the loop

        except Exception as e:
            print(e)
            print("invalid input")  # this will display when the player makes a typo mistake

    print("game over")


def player_selection():    # define another function for the number of players to play
    while True:  # by using this step the game will only stop if the given condition will be true
        try:
            print("Welcome to the guessing game")
            players = int(input("you can play up to 4 players and to close this game press 5"
                                "\nplease select the number of players:-\n"))  # player selection

            if players == 1:
                guessing_game()  # calling the function
                break

            elif players == 2:
                print("First player turn")
                guessing_game()
                print("Second player turn")
                guessing_game()
                break         # the game will end when all the players have taken their turns

            elif players == 3:
                print("First player turn")
                guessing_game()
                print("Second player turn")
                guessing_game()
                print("Third player turn")
                guessing_game()
                break

            elif players == 4:
                print("First player turn")
                guessing_game()
                print("Second player turn")
                guessing_game()
                print("Third player turn")
                guessing_game()
                print("Forth player turn")
                guessing_game()
                break

            elif players == 5:
                print("Thank you playing")
                break

            else:
                print("invalid input")

        except Exception as e:
            print(e)
            print("something went wrong")


player_selection()    # to play this game call the player selection function

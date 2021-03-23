import random

guessNumber = random.randint(0, 100)

numOfGuesses = 0

inGame = True

while inGame:
    print("What Is Your Guess")
    userGuess = int(input())
    if userGuess == guessNumber:
         inGame = False
         break
    elif userGuess > guessNumber:
        print("Your Guess is Higher than the Actual Number.")
    else:
        print("Your Guess Is Lower Than The Actual Number.")
    numOfGuesses = numOfGuesses + 1 

print("It Took You", numOfGuesses, "Guesses, Well Done!")
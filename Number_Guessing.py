import random
def guessgame(guess,number):
    if guess > number:
        if guess - number < 10:
            print("You're close but high. Try again")
            return
        else:
            print("Too high. Try again")
            return
    elif guess < number:
        if number - guess <10:
            print("You're close but low. Try again")
            return
        else:
            print("Too low. Try again")
            return
    elif guess == number:
        print(f"You got it! You guessed the right number: {number}!")
        return
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1,100)
print(f"Psst, the correct answer is {number}")
level = input("Choose a difficulty. Type 'easy or 'hard': ").lower()
if level == 'easy':
    chances = 10
elif level == 'hard':
    chances = 5
else:
    print("Option is invalid!")
while True:
    print(f"You have {chances} chances left.")
    guess = input("Make a guess: ")
    guessgame(int(guess),int(number))
    if guess == number:
        exit()
    else:
        chances -=1
    if chances == 0:
        print("You're out of guesses. You lose")
        exit()







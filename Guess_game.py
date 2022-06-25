import random
jackpot = random.randint(1,500)
guess = int(input("Guess a number: "))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Guess higher")
    else :
        print("Guess lower")
    guess = int(input("Guess a number: "))
    counter += 1
print("Correct Answer")
print("you took", counter, "attempts")

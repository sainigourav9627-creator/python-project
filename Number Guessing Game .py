import random

play = "yes"

while play == "yes":

    secret_number = random.randint(1,10)

    attempt = 0

    while attempt < 5:
        guess = int(input("Enter the guess number: "))

        attempt = attempt + 1

        if guess == secret_number:
            print("You Win")
            print("Total Attempts:", attempt)
            break

        elif guess < secret_number:
            print("Number is too small")

        else:
            print("Number is too high")

    else:
        print("Game Over")
        print("Secret Number was:", secret_number)

    play = input("Play Again? yes/no: ")

print("Thanks for Playing")



or 




import random

secret_number = random.randint(1,10)

guess = int(input("Enter Guess: "))

if guess == secret_number:
    print("You Win")
else:
    print("You Lose")

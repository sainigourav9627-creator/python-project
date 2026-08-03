import random

secret_number = random.randint(1,10)

attempt = 0

while True:
    guess = int(input("Enter the guess number: "))
    
    attempt = attempt + 1
    
    if guess == secret_number:
        print("You Win")
        break
    else:
        print("Wrong Guess")

print("Total Attempts :", attempt)

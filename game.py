import random
secret_number = random.randint(1,10)
attempts = 0
while True:
    try:
        guess = int(input("guess a number between 1 and 10: "))
        attempts += 1
        if guess == secret_number:
            print ("you win", 
                   "attempts:", attempts)
            break
        elif guess < secret_number:
            print ("too low, try again")
        else:
            print ("too high, try again")
    except ValueError:
        print ("please enter a valid number.")

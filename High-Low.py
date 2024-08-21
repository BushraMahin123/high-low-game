import random
print("welcome to the High Low game")
count = 1
score = 0
while count < 6:  
    print(f"Round {count}")
    print("--------------------------------")
    random_number : int = random.randint(1,100)
    player2_number : int = int(input("Your number is: "))
    guess : str = input("Do you think your number is higher or lower than the computer's?:")

    if(random_number > player2_number):
        if(guess == "higher"):
            print(f"You lose the computer's number is {random_number}")
        else:
            print(f"Yayyy! You won the computer's number is {random_number}")
            score+=1
    else:
        if(guess == "higher"):
            print(f"Yayyy! You won the computer's number is {random_number}")
            score+=1
        else:
            print(f"You lose the computer's number is {random_number}")
    count += 1  

print(f"Your total score {score}")

if(score < 2):
    print("You won less than half the rounds")
elif(score == 2):
    print("You  won at least half the rounds (rounded down)")
else:
    print("Wow! You played perfectly!")


print("Thanks for playing!!")

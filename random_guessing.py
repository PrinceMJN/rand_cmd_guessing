import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Enter a number larger than 0 next time")
        quit()
else:
    print("Enter a number next time")
    quit()
random_num = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
       user_guess = int(user_guess)
       #print(random_num)
    else:
        print("Enter a number next time.")
        continue
    if user_guess == random_num:
        print("Correct, You got it!")
        break
    else:
        #print("you got it wrong")
        if user_guess > random_num:
            print("you were above the number")
        else:
            print("you were below the number")
print("You got it in " + str(guesses) +" guesses")


print("Welcome to my simple quiz game.")

name = input("What is your name? ")

print("Welcome " + str(name))

yesorno = input("Do you wanna play a quick Quiz game? ")

if yesorno.lower() != "yes":
    quit()

else:
    print("Lets start.")
    score = 0

answer = input("How many days are there in a week? ")
if answer.lower() == "7 days":
    print("Yayy, thats Correct :)")
    score += 1
else:
    print("Sorry, Thats incorrect")

answer = input("How many hours are there in a day? ")
if answer.lower() == "24 hours":
    print("Yayy, thats Correct :)")
    score += 1
else:
    print("Sorry, Thats incorrect")

answer = input("When is Christmas? ")
if answer.lower() == "25 december":
    print("Yayy, thats Correct :)")
    score += 1
else:
    print("Sorry, Thats incorrect")

answer = input("How many days are there in a year? ")
if answer.lower() == "365 days":
    print("Yayy, thats Correct :)")
    score +=1
else:
    print("Sorry, Thats incorrect")


print("You got "+str(score)+ " answer right")

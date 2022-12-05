import random
rand=random.randint(1,100)
print("THIS IS A NUMBER GUESSING GAME")
chance=3
score=0
while(chance!=0):
    num = int(input("Guess a number between 1 to 100: "))

    if(num == rand):
        print("Congrat's")
        score+=10
        print("You score",score)
        chance-=1
    elif(num > rand):
        print("Have one more try, Your guess was too samll")
        chance-=1
    else:
        print("Have one more try, Your guess was too samll")
        chance-=1

    if(chance==0):
        print("your total score is",score)

print("Better Luck Next Time!")
print("The number was: ",rand)
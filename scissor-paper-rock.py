#rock paper scissor game
import random
user_score=0
CPU_score=0



name= input("Enter Your Name Here:")
print("Welcome To Our Game",name)
print("GAME RULE'S")
print("""
 1. Rock > Scissors
 2. Paper > Rock
 3. Scissors > Paper 
 """)
while True:
    print("""Choices are
        1. Rock
        2. Paper
        3. Scissors""")
    choice=int(input("Enter Your Choice from 1-3:"))
    print()


    if choice>3 or choice<1:
        choice=input("Please Enter The Valid Input")

    if choice==1:
        user_input="Rock"
    elif choice == 2:
        user_input="Paper"
    else:
        user_input="Scissors"

    print("THE USER INPUT IS:",user_input)


    CPU=random.randint(1,3)
    if CPU== 1:
        CPU_input="Rock"
    elif CPU== 2:
        CPU_input="Paper"
    else:
        CPU_input="Scissors"
    print("THE CPU SELECTS:",CPU_input)
    #CASE 1 user wins
    if (user_input== "Paper" and CPU_input == "Rock") or (user_input == "Rock" and CPU_input == "Paper"):
         if user_input=="Paper":
             print("User wins")
         else:
             print("CPU wins")
         result= "paper"
    elif (user_input== "Scissors" and CPU_input == "Rock") or (user_input == "Rock" and CPU_input == "Scissors"):
        if user_input == "Scissors":
            print("User wins")
        else:
            print("CPU wins")

        result= "Rock"

    elif (user_input== "Scissors" and CPU_input == "Paper") or (user_input == "Paper" and CPU_input == "Scissors"):
        if user_input == "Scissors":
            print("User wins")
        else:
            print("CPU wins")
        result = "Scissors"
    else:
        print("It's a Tie")
        result= "Tie"

    #to print tie
    if result == "Tie":
        ties=+1
    elif result == user_input:
        user_score+=1

    else:
        CPU_score+=1

    print("Scores are:")
    print(name,"s scores are", user_score)
    print("CPU scores are", CPU_score)

    new_game=input("DO YOU WANT TO PLAY AGAIN?")
    if new_game== "NO" or new_game== "No" or  new_game== "no":
        print("Final scores are:")
        print(name, "s scores are", user_score)
        print("CPU scores are", CPU_score)
        break
print("GAME IS OVER")
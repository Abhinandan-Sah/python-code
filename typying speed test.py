from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
              error = error + 1
    return error



def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = (time_delay)
    speed = len(userinput)/time_R
    return round(speed)




while True:
    ck = input("ready to test : yes / no : ")
    if ck=="no":
        print("Thank you")
        break
    elif (ck=="yes"):
     test=["Hello python how are you what are you duing you are great and simple and allso intresting","my name is satyam tiwari i am user","i am typing and "]
     test1=r.choice(test)
     print("        ***** typing speed *****")
     print(test1)
     print()
     print()
     time_1 = time()
     testinput=input(" Enter : ")
     time_2 = time()


     print("Speed : ",speed_time(time_1,time_2,testinput)," w/sec")
     print("Error : ",mistake(test1,testinput))
    else:
        print("wrong input")




class Car:
    #Add attributes
    name=None
    color = None
    # Adding a method
    def get_Speed(self):
        name="Honda City"
        color='Red'
        return name+" is available in "+color+"color"

#creating an instance of as Honda
Honda=Car()
print(Honda.get_Speed())


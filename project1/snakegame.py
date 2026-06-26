computer = 1
youstr =  input("enter the choice: ")
youDict = {"s":1, "w":2 , "g":3}
you = youDict(youstr)

if(computer == 1 and you == 2):
    print("You loss")

elif(computer == 1  and you==3):
    print("You win")   
elif(computer == 1 and you==1):
    print("Game Draw")  
elif(computer == 2 and you==2):
    print("Game Draw") 
elif(computer == 3 and you==3):
    print("Game Draw") 
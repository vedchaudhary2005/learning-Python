marks1 = int(input("enter the marks 1: "))
marks2 = int(input("enter the marks 2: "))
marks3 = int(input("enter the marks 3: "))


percentage = (100*(marks1 + marks2 + marks3)) /300
if(percentage <= 40):
    print("you r pass", percentage)
elif(percentage <= 23):
    print("You r fail", percentage)
elif(percentage > 70):
    print("Good sabash", percentage)
import random


computer = random.randint(1, 3)
youstr = input("Enter your choice (s for Stone, w for Water, g for Gun): ")


youDict = {"s": 1, "w": 2, "g": 3}

you = youDict[youstr]


print("Computer chose:", computer)
print("You chose:", you)

if computer == 1 and you == 2:
    print("You Lose")

elif computer == 1 and you == 3:
    print("You Win")

elif computer == 1 and you == 1:
    print("Game Draw")

elif computer == 2 and you == 1:
    print("You Win")

elif computer == 2 and you == 3:
    print("You Lose")

elif computer == 2 and you == 2:
    print("Game Draw")

elif computer == 3 and you == 1:
    print("You Lose")

elif computer == 3 and you == 2:
    print("You Win")

elif computer == 3 and you == 3:
    print("Game Draw")
import random
def game():
    print("You r playng the game..")
    score =  random.randint(1, 61)
    print(f"Your Score: {score}")
    if(score>highscore or highscore==""):
        print("  ")
    return score
game()
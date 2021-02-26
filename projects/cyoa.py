from random import randint
points: int = int(1)
player: str = ""
THUMBS_UP: str = "\U0001F44D"
SCARED_FACE: str = "\U0001F61F"
DRAGON: str = "\U0001F409"
SAD: str = "\U0001F622"
FLOWERS: str = "\U0001F490"
TROLL: str = "\U0001F5FF"



def main() -> None:
    """Entry point of program."""
    greet()
    print("Choose option 1, 2, or 3")
    global points
    first_choice: int = int(input(f"1: Leave game 2: Enter CREEPY LAIR {SCARED_FACE} 3: Enter FLOWER GARDEN {FLOWERS} "))
    if first_choice < 2:
        print(f"Goodbye. You gained {points} adventure points.")
    else:
        if first_choice < 3:
            creepy_lair()
            final_stage()
        else:
            if first_choice == 3:
                points = int(flower_garden(points)) 
                print(f"Your point total is {points}.")
                final_stage()



def greet() -> None:
    """Function to introduce player."""
    global player
    player = (input("Welcome PLAYER what is your name? "))
    print(f"Hello {player} in this story game you will make decisions that will decide if you WIN {THUMBS_UP} or LOSE {SAD}")
    global points
    print(f"You have {points} points.")



def creepy_lair() -> None:
    """A function with a troll encounter"""
    joke: str = str(input(f"You encounter a troll {TROLL} who wants to be a stand-up comic. Do you want to hear his jokes yes/no "))
    global points
    if joke == "yes":
        points += 50
        print(f"Congradulations {player}. You made the troll HAPPY {THUMBS_UP}! New point total is {points}!")
    else:
        points = points - 1
        print(f"Oh no {player}! You made the troll SAD {SAD}. He BONKS you. Your point total is {points}")



def flower_garden(p: int) -> int:
    print(f"Silly {player}! You're allergic to flowers {FLOWERS}. You DIED")
    cont: str = str(input("Would you like to keep playing? (yes/no)"))
    if cont == "yes":
        p = p - 99
    else:
        p = p - 100
        print("Haha you must continue. Free will is an illusion.")
    return p



def final_stage() -> None:
    """This is level for above and beyond points"""
    pick_a_number: int = randint(1,6)
    print(f"You are challenged by a mystical creature {DRAGON} to predict a number rolled on a die.")
    guess: int = int(input("What is your guess? (Pick a number 1-6)"))
    if pick_a_number == guess:
        global points
        points += 100
        print(f"CONGRADULATIONS {player} you WIN! Your point total is {points}.")
    else:
        print(f"Oops you lose {SAD}. Better luck next time. Your point total is {points}.")
    while input("Would you like to play again? (yes/no)") == "yes":
        """This is where I loop the game for above and beyond points"""
        main()




if __name__ == "__main__":
  main()
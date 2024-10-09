from random import randint

#Function Definitions#
def print_instructions():
    print("\n\nWelcome to Rock, Paper, Scissors!\n")
    print("Rock, Paper, Scissors is a simple hand game played between two people. Each player simultaneously chooses one of three options: rock, paper, or scissors.\nThe winner of each round is determined by the following rules:\n\n  - Rock (🪨 ) beats Scissors (✂️  ) because rock can crush scissors.\n  - Scissors (✂️  ) beats Paper (📄 ) because scissors can cut paper.\n  - Paper (📄 ) beats Rock (🪨  ) because paper can wrap around rock.\n\nIf both players choose the same option, the round is a tie. The game is typically played in multiple rounds, and the player with the most wins at the end is the overall winner.\n\n")

def start_game():
    name = input("Enter your name: ")
    rounds = int(input("How many rounds do you want to play? "))
    print("Starting game...")
    return name, rounds

def get_player_choice(name):
    throw1 = ""
    while throw1 not in ("rock", "paper", "scissors"):
        throw1 = input(f"{name}, what would you like to throw? ").lower()

    if throw1 == "rock":
        throw1 = "🪨"
    elif throw1 == "scissors":
        throw1 = "✂️"
    else:
        throw1 = "📄"

    print(f"You chose {throw1}")
    return throw1

def get_cpu_choice():
    print("Computer choosing...")
    cputhrow1 = randint(1, 3)

    if cputhrow1 == 1:
        cpuchoice1 = "🪨"
    elif cputhrow1 == 2:
        cpuchoice1 = "✂️"
    else:
        cpuchoice1 = "📄"

    print(f"Cpu chose {cpuchoice1}")
    return cpuchoice1

def throw_statements(throw1, cpuchoice1, plyr_score, cpu_score, count):
    rock, paper, scissors = "🪨", "📄", "✂️"
    
    # Rock statements
    if throw1 == "🪨" and cpuchoice1 == "✂️":
        print(f"You won this round because {rock} beats {scissors}.")
        plyr_score += 1
    elif throw1 == "🪨" and cpuchoice1 == "🪨":
        print(f"You tied this round because {rock} cancels out {rock}.")
    elif throw1 == "🪨" and cpuchoice1 == "📄":
        print(f"You lost this round because {rock} loses to {paper}.")
        cpu_score += 1

    # Scissors statements
    if throw1 == "✂️" and cpuchoice1 == "📄":
        print(f"You won this round because {scissors} beats {paper}.")
        plyr_score += 1
    elif throw1 == "✂️" and cpuchoice1 == "✂️":
        print(f"You tied this round because {scissors} cancels out {scissors}.")
    elif throw1 == "✂️" and cpuchoice1 == "🪨":
        print(f"You lost this round because {scissors} loses to {rock}.")
        cpu_score += 1

    # Paper statements
    if throw1 == "📄" and cpuchoice1 == "🪨":
        print(f"You won this round because {paper} beats {rock}.")
        plyr_score += 1
    elif throw1 == "📄" and cpuchoice1 == "📄":
        print(f"You tied this round because {paper} cancels out {paper}.")
    elif throw1 == "📄" and cpuchoice1 == "✂️":
        print(f"You lost this round because {paper} loses to {scissors}.")
        cpu_score += 1

    count += 1
    print(f"The score is {plyr_score} - {cpu_score}")
    return plyr_score, cpu_score

# Main Program#
print_instructions()

count = 0
plyr_score = 0
cpu_score = 0

name, rounds = start_game()

while count < rounds:
    throw1 = get_player_choice(name)
    cpuchoice1 = get_cpu_choice()
    plyr_score, cpu_score = throw_statements(throw1, cpuchoice1, plyr_score, cpu_score, count)
    count += 1

if plyr_score > cpu_score:
    print(f"You won the game! Final score: {plyr_score} - {cpu_score}")
elif plyr_score < cpu_score:
    print(f"You lost the game. Final score: {plyr_score} - {cpu_score}")
else:
    print(f"It's a tie! Final score: {plyr_score} - {cpu_score}")

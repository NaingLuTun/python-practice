import random



win = False
lose = False

while win == False and lose == False:
    npc_random_choice = random.randint(1, 3)
    player_choice = input("Lets play rock paper scissors\n Choose your weapon.\n \"r\" for rock\n \"p\" for paper\n \"s\" for scissors\n\n ")

    # Check for valid input
    if player_choice.lower() in ("r", "p", "s"):
        if npc_random_choice == 1 and player_choice == "r":
            print("The computer chose rock")
            print("You drew")
        elif npc_random_choice == 1 and player_choice == "p":
            print("The computer chose rock")
            win = True
        elif npc_random_choice == 1 and player_choice == "s":
            print("The computer chose rock")
            lose = True
        if npc_random_choice == 2 and player_choice == "r":
            print("The computer chose paper")
            lose = True
        elif npc_random_choice == 2 and player_choice == "p":
            print("The computer chose paper")
            print("You drew")
        elif npc_random_choice == 2 and player_choice == "s":
            print("The computer chose paper")
            win = True
        if npc_random_choice == 3 and player_choice == "r":
            print("The computer chose scissors")
            win = True
        elif npc_random_choice == 3 and player_choice == "p":
            print("The computer chose scissors")
            lose = True
        elif npc_random_choice == 3 and player_choice == "s":
            print("The computer chose scissors")
            print("You drew")
    else:
        print("Invalid input. Please choose 'r', 'p', or 's'.")

if win:
    print("You won!")
elif lose:
    print("You lost!")
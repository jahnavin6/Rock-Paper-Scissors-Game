import time
loose = ("System wins")
win = ("User Wins")
lives = 3
score = 0
drew = 0
computer_lives = 5
pwdmatches = []
while True:
    username = input("Enter ID -  ")
    password = input("Enter Password -  ")
    dest = open("name.txt","r")
    for inp in dest:
        pwdmatches.append(inp.strip())
        if username and password in pwdmatches:
                print("Login Successful !!")
                time.sleep(0.5)
                print("Loading.")
                time.sleep(0.5)
                print("Loading..")
                time.sleep(0.5)
                print("Loading...")
                time.sleep(0.5)
                start_menu = """


"""
                print(start_menu)
                while True:
                    game = input("Rock, Paper, Scissors?   ")
                    game = game.title()
                    import random
                    computer = ("rock", "paper", "scissors")
                    computer = random.choice(computer)
                    #rock if statments
                    if game == "Rock" and computer == "paper":
                        print("The computer choose",computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives-=1
                    if game == "Rock" and computer == "scissors":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        print("")
                        print("")
                        score+=1
                  #paper if statements
                    if game == "Paper" and computer == "rock":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score+=1
                    if game == "Paper" and computer == "scissors":
                        print("The computer choose",computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives-=1
                    #scissor if statements
                    if game == "Scissors" and computer == "paper":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score+=1
                    if game == "Scissors" and computer == "rock":
                        print("The computer choose",computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives-=1
                    #duplicates
                    if game == "Rock" and computer == "rock":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1               
                    if game == "Paper" and computer == "paper":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1
                    if game == "Scissors" and computer == "scissors":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1
                    #system
                    if game == "rules":
                        print("**********************************************")
                        print("Rules")
                        print("**********************************************")
                        print("-Rock looses against Paper")
                        print("-Rock beats Scissors")
                        print("-Paper beats Rock")
                        print("-Paper looses against Scissors")
                        print("-Scissors beats Paper")
                        print("-Scissors looses against Rock")
                        print("**********************************************")
                    if game == "display lives":
                        print(lives)
                    if game == "display score":
                        print(score)
                    if game == "display drew":
                        print(drew)
                    #lives
                    if lives == 0 or game == "test":
                        print("Game Over!!")
                        print("You got",score,"correct")
                        print("You drew",drew,"times")
                        stop = input("Press enter to exit.")
                        exit()
                    if computer_lives == 0:
                        print("User Wins.")
                        print("You got",score,"correct")
                        print("You drew",drew,"times")
                        stop = input("Press enter key to exit.")
                        exit()
                    #exit
                    if game == "exit":
                        break
        if password in inp and password != inp:
            print("Your username or password is incorrect.")
            print("---------------------------------------")

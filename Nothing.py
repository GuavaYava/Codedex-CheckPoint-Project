import random
def main():
    #Text
    print('===================')
    print('Rock Paper Scissors')
    print('=================== \n')
    print("(1) Rock ✊")
    print("(2) Paper ✋")
    print("(3) Scissors ✌️ \n")

    #Taking user input (does not account for invalid input, for now)
    while True:
        try:
            user_choice = int(input("Enter your choice (1-3): "))
            break
        except:
                print("Please enter a number only")
    if user_choice == 1:
        user_choice_name = 'Rock'
    elif user_choice == 2:
        user_choice_name = 'Paper'
    elif user_choice == 3:
        user_choice_name = 'Scissors'

    print(f"\nYou chose: {user_choice_name}")

    #Getting the computer's choice
    pc_choice = random.randint(1, 3)
    if pc_choice == 1:
        pc_choice_name = 'Rock'
    elif pc_choice == 2:
        pc_choice_name = 'Paper'
    elif pc_choice == 3:
        pc_choice_name = 'Scissors'

    print(f"Computer chose: {pc_choice_name}")

    #Win or Lose (elif block😭)
    if(pc_choice == 1 and user_choice == 1):
        print("Tie!")
    elif(pc_choice == 1 and user_choice == 2):
        print("You Win!")
    elif(pc_choice == 1 and user_choice == 3):
        print("PC Wins!")
    elif(pc_choice == 2 and user_choice == 2):
        print("Tie!")
    elif(pc_choice == 2 and user_choice == 3):
        print("You Win!")
    elif(pc_choice == 2 and user_choice == 1):
        print("PC Wins!")
    elif(pc_choice == 3 and user_choice == 3):
        print("Tie!")
    elif(pc_choice == 3 and user_choice == 2):
        print("You Win!")
    elif(pc_choice == 3 and user_choice == 1):
        print("PC Wins!")
        
#Start
start = input("Would you like to start the game? (Yes/No): ")
if start.lower().strip() == "yes":
    main()
    #Ask to play again
    yes = True
    while(yes):
        play_again = input("Would you like to play again? (Yes/No): ")
        if play_again == start.lower().strip() == "yes":
            main()
        else:
            yes = False
else:
    print("You didn't say yes so I won't start")



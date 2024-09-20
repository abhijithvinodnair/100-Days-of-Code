import random
 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Game = [rock, paper, scissors]
while True:
    print ("Welcome to Rock Paper Scissors!")
    your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
    if your_choice < 0 or your_choice > 2:
        print("Invalid choice! Try again.")
        exit
    else:
        print(your_choice)
        computer_choice = random.randint(0, 2)

        if Game[your_choice] == Game[computer_choice]:
            print(f"Your Choice:\n{Game[your_choice]} \nComputer chose:\n{Game[computer_choice]}\nIt's a draw!")
        elif Game[your_choice] > Game[computer_choice]:
            if your_choice == 0 and computer_choice == 2:
                print(f"Your Choice:\n{Game[your_choice]} \nComputer chose:\n{Game[computer_choice]}\nYou win!")
            else:
                print(f"Your Choice:\n{Game[your_choice]} \nComputer chose:\n{Game[computer_choice]}\nComputer wins!")
        elif Game[your_choice] < Game[computer_choice]:
            if your_choice == 2 and computer_choice == 0:
                print(f"Your Choice:\n{Game[your_choice]} \nComputer chose:\n{Game[computer_choice]}\nComputer wins!")
            else:
                print(f"Your Choice:\n{Game[your_choice]} \nComputer chose:\n{Game[computer_choice]}\nYou win.")

    if input("Do you want to stop? playing (yes/no): ").lower() == "yes":
        break






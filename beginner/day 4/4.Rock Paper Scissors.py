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

#Write your code below this line 👇
import random
your_choise=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choise=random.randint(0,2)
symbol=[rock,paper,scissors]
if your_choise<=2:
    print(symbol[your_choise])
    print(symbol[computer_choise])
    if your_choise==0 and computer_choise==2:
        print ("you win")
    elif your_choise==1 and computer_choise==0:
        print("you win")
    elif your_choise==2 and computer_choise==1:
        print("you win")
    elif your_choise==computer_choise:
        print("it's a drow")
    else:
        print("you loose")
else:
    print("you type invalid number")
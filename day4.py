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

user=int(input("what did you choose?  type 0 for rock, 1 for paper or 2 for scissors:\n"))
if user  ==0:
    print("rock\n",rock)
elif user  ==1:
    print("paper\n",paper)
else :
    print("scissors\n",scissors)


value= int(random.randint(0,2))
if value  == 0:
    print("computer choose: rock\n",rock)
elif value  ==1:
    print("computer choose: paper\n",paper)
else:
    print("computer choose: scissors\n",scissors)

if user==0 and value==2:
    print("you won")
elif user==1 and value==0:
    print("you won")
elif user==2 and value==1:
    print("you won")
elif user==value:
    print("draw")
else:
    print("you lose")

    
























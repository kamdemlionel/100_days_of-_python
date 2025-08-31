from game_data import data
from art import logo, vs
import random
end_of_game=False

print(logo)
A= random.choice(data)
B=random.choice(data)
score=0
def first():
    print("compare A:",A["name"],A["description"],A["country"])
    print(vs)
    print("against B:",B["name"],B["description"],B["country"])
def second():
    global score 
    choice=input("who has more followers?")
    
    if choice=="B" and B["follower_count"]>A["follower_count"]:
       print("you won")
       score+=1
       return True
    elif choice=="A" and A["follower_count"]>B["follower_count"]:
        print("you won")
        score+=1
        return True
    else:
        print("you lose")
        return False

while not end_of_game:
    first()
    result=second()
    print("your score is ",score)
    if not result:
        end_of_game = True
    else:
        A = B
        # Ensure new B is not same as A
        B = random.choice(data)
        while B == A:
            B = random.choice(data)
        

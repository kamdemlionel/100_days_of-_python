import os
import art
print(art.logo)



dictionary={}
def bidding():
    name= input("enter your name: ")
    bid= int(input("what is your bid?: "))
    final={name:bid}
    dictionary.update(final)


print(art.logo)
bidding()
choice=input("do you want another bid?: ")


while choice=="yes":
    os.system("clear")
    bidding()
    choice=input("do you want another?")
else:
    winner=max(dictionary, key=dictionary.get)
    highest=dictionary[winner]

    print("the highest bid is ",winner,"with ", highest)
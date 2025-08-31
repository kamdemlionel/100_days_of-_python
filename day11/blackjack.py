############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

# import random


# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# black_jack=[11,10]
# ace=[1,11]


# user_cards=[]
# computer_cards=[]



# def select_user_card():
#     selected=random.sample(cards,2)
#     global user_cards
#     user_cards=selected
    
# def select_comp_card():
#     comp_selected=random.sample(cards,2)
#     global computer_cards
#     computer_cards=comp_selected

# question=input("do you want to play a game of blackjack? type yes or No:  ")
    
# if question=="yes":
#     select_user_card()
#     select_comp_card()
    
# else:
#     print("goodbye")

# current_score=sum(user_cards)
# print("your cards: ",user_cards,"current_score: ", current_score)
# print("computer cards", computer_cards[0])
# if user_cards!=black_jack or computer_cards!=black_jack:
#     if current_score>21:
#         if ace in user_cards:
#             ace=1
#             if current_score>21:
#                 print("you lose")
                


#     print("user has blackjack")
# elif computer_cards==black_jack:
#     print("user has blackjack")
# else:currenct
import streamlit as st
import random

# Function to deal a card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Function to calculate score
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Function to compare scores
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# Streamlit UI
st.title("♠️ Blackjack Game 🃏")
st.write("Try to beat the computer without going over 21!")

# Initialize session state
if "user_cards" not in st.session_state:
    st.session_state.user_cards = []
if "computer_cards" not in st.session_state:
    st.session_state.computer_cards = []
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "result" not in st.session_state:
    st.session_state.result = ""

# Function to start/reset game
def start_game():
    st.session_state.user_cards = [deal_card(), deal_card()]
    st.session_state.computer_cards = [deal_card(), deal_card()]
    st.session_state.game_over = False
    st.session_state.result = ""

# Function for user to draw a card
def hit():
    st.session_state.user_cards.append(deal_card())
    user_score = calculate_score(st.session_state.user_cards)
    if user_score > 21:
        st.session_state.game_over = True
        end_game()

# Function to end game
def end_game():
    user_score = calculate_score(st.session_state.user_cards)
    computer_score = calculate_score(st.session_state.computer_cards)

    while computer_score != 0 and computer_score < 17:
        st.session_state.computer_cards.append(deal_card())
        computer_score = calculate_score(st.session_state.computer_cards)

    st.session_state.result = compare(user_score, computer_score)
    st.session_state.game_over = True

# Buttons
if st.button("Start New Game"):
    start_game()

if st.session_state.user_cards:
    user_score = calculate_score(st.session_state.user_cards)
    computer_score = calculate_score(st.session_state.computer_cards)

    st.subheader("Your Hand:")
    st.write(st.session_state.user_cards, f"Score: {user_score}")

    st.subheader("Computer's Hand:")
    if st.session_state.game_over:
        st.write(st.session_state.computer_cards, f"Score: {computer_score}")
    else:
        st.write([st.session_state.computer_cards[0], "❓"])

    if not st.session_state.game_over:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Hit (Draw a Card)"):
                hit()
        with col2:
            if st.button("Stand"):
                end_game()

    if st.session_state.result:
        st.success(st.session_state.result)

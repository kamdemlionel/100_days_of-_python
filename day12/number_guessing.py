# import random 
# guessed_number=random.randint(0,100)
# print("welcome to the world guessing game ")
# level=input("which level of difficulty do you want, easy or hard ")

# attempts=10

# def attempts_left():
#     global attempts
#     attempts-=1
#     return attempts
    

# def guessed():
#     guess=int(input("guess the  number"))
#     if guess>guessed_number:
#         attempts_left()
#         print(f"it is greater, you are left with {attempts}")
        
#     elif guess<guessed_number:
#         attempts_left()
#         print(f"it is lower, you are left with {attempts}")
        
#     else:
#         print(f"Congratulations! You guessed the number {guessed_number} correctly in {attempts} attempts.")

# if level=="hard":
#     attempts=5
#     while attempts!=0:
#         guessed()
#     else:
#         print("you lose")
# elif level=="easy":
#     attempts=10
#     while attempts!=0:
#         guessed()
#     else:
#         print("you lose")
# else:
#     print("enter valid input ")

import streamlit as st
import random

st.title("🎯 Number Guessing Game")
st.write("Welcome to the World Guessing Game!")

# Initialize session state variables
if "guessed_number" not in st.session_state:
    st.session_state.guessed_number = random.randint(0, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_active" not in st.session_state:
    st.session_state.game_active = False
if "message" not in st.session_state:
    st.session_state.message = ""

# Difficulty selection
if not st.session_state.game_active:
    level = st.radio("Choose difficulty:", ["Easy", "Hard"])
    if st.button("Start Game"):
        st.session_state.guessed_number = random.randint(0, 100)
        st.session_state.attempts = 10 if level == "Easy" else 5
        st.session_state.game_active = True
        st.session_state.message = f"You have {st.session_state.attempts} attempts left. Start guessing!"
        st.rerun()

# Game play
if st.session_state.game_active:
    st.info(st.session_state.message)

    guess = st.number_input("Enter your guess (0 - 100):", min_value=0, max_value=100, step=1)

    if st.button("Submit Guess"):
        if st.session_state.attempts > 0:
            if guess > st.session_state.guessed_number:
                st.session_state.attempts -= 1
                st.session_state.message = f"Too high! Attempts left: {st.session_state.attempts}"
            elif guess < st.session_state.guessed_number:
                st.session_state.attempts -= 1
                st.session_state.message = f"Too low! Attempts left: {st.session_state.attempts}"
            else:
                st.success(f"🎉 Congratulations! You guessed the number {st.session_state.guessed_number}!")
                st.session_state.game_active = False

        if st.session_state.attempts == 0 and guess != st.session_state.guessed_number:
            st.error(f"💀 You lose! The number was {st.session_state.guessed_number}.")
            st.session_state.game_active = False

        st.rerun()

# Restart option
if not st.session_state.game_active and st.button("Play Again"):
    st.session_state.guessed_number = random.randint(0, 100)
    st.session_state.attempts = 0
    st.session_state.message = ""
    st.rerun()

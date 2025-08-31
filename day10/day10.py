import streamlit as st


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2


operations = {
    "Add": add,
    "Subtract": subtract,
    "Multiply": multiply,
    "Divide": divide
}


st.title("🧮 Simple Calculator")


num1 = st.number_input("Enter the first number:", value=0.0, step=1.0)
operation = st.selectbox("Choose an operation:", list(operations.keys()))
num2 = st.number_input("Enter the second number:", value=0.0, step=1.0)

# Calculate button
if st.button("Calculate"):
    calculation_function = operations[operation]
    result = calculation_function(num1, num2)
    st.success(f"{num1} {operation} {num2} = {result}")

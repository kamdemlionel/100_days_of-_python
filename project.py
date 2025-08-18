print("welcome to the tip calculator")
total_bill= float(input("what was the total bill?\n"))
percentage_tip = int(input("what percentage tip would you like to give 10,12, or 15?\n"))
tip= total_bill *(percentage_tip/100)
final_amount= total_bill + tip
print(f"Your final bill including the tip is: {final_amount}")

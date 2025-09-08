# from carte import MENU, resources
# command=input("​What would you like? (espresso/latte/cappuccino):​")
# water=resources["water"]
# milk=resources["milk"]
# coffee=resources["coffee"]



# if command=="report":
#     print(f" water={water}\n milk={milk}\n coffee={coffee}" )
# def check_resource(cmd):
#     if resources["water"]<MENU[cmd]["ingredients"]["water"]:
#         print("sorry there is not enough water")
#         return False
#     elif resources["milk"]<MENU[cmd]["ingredients"]["milk"]:
#         print("sorry there is not enough milk")
#         return False
#     elif resources["coffee"]<MENU[cmd]["ingredients"]["coffee"]:
#         print("there is not enough milk")
#         return False
#     else:
#         return True
# def check_sufficient(cmd):
#     if total<MENU[cmd]["cost"]:
#         print("​Sorry that's not enough money. Money refunded.")
#         return False
#     elif total==MENU[cmd]["cost"]:
#         print(f"water={MENU[cmd]["ingredients"]["water"]}\n milk={MENU[cmd]["ingredients"]["milk"]}\n coffee={MENU[cmd]["ingredients"]["coffee"]} cost={MENU[cmd]["cost"]} ")
#         return True
#     else:
#         print(f"water={MENU[cmd]["ingredients"]["water"]}\n milk={MENU[cmd]["ingredients"]["milk"]}\n coffee={MENU[cmd]["ingredients"]["coffee"]} cost={MENU[cmd]["cost"]} ")
#         change=total-MENU[cmd]["cost"]
#         print("your change is:  ",change)
#         return True
    
# def deduction(cmd):
#     if check_sufficient(command)==True:
#         water=resources["water"]-MENU[cmd]["ingredients"]["water"]
#         milk=resources["milk"]-MENU[cmd]["ingredients"]["milk"]
#         coffee=resources["coffee"]-MENU[cmd]["ingredients"]["coffee"]
#         print(f" water={water}\n milk={milk}\n coffee={coffee}")

# if check_resource(command)==True:
#     print("insert a coin")
#     quarters_amt=int(input("how many quarters"))
#     dimes_amt=int(input("how many dimes"))
#     nickles_amt=int(input("how many nickles"))
#     pennies_amt=int(input("how many pennies"))
#     total=(quarters_amt*0.25)+(dimes_amt*0.10)+(nickles_amt*0.05)+(pennies_amt*0.01)
#     print(total)
#     check_sufficient(command)
#     deduction(command)
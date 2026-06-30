print("Welcome to the Budget Tracker, where you can monitor your monthly expenses and savings!")

name = input("Enter your name: ")

monthly_income = float(input("What is your monthly income?: "))
rent_expense = float(input("What is your monthly expense on your rent?: "))
food_expense = float(input("What is your monthly expense on your food?: "))
travel_expense = float(input("What is your monthly expense on your travel?: "))

total_expense = rent_expense + food_expense + travel_expense
print(f"Your monthly expense will be {total_expense}.")

money_remaining = monthly_income - total_expense
print(f"Your monthly savings will be {money_remaining}.")

savings_percentage = round((money_remaining / monthly_income) * 100, 2)
print(f"Your monthly savings percentage will be {savings_percentage}%.")

if savings_percentage >= 20:
    print("You are saving enough money!")
else:
    print("You need to save more money!")


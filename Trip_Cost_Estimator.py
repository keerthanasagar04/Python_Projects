print("Hey! I am gonna estimate total cost for your trip.")

city = input("Which city are you going to visit?: ")
number_of_days = float(input("How many days are you planning to travel?: "))
hotel_cost = float(input("What will be the cost of hotel per day?: "))
food_budget = float(input("What is your daily food budget?: "))
traveling_expense = float(input("What is your daily traveling expense?: "))
number_of_people = int(input("How many people are travelling? "))
budget = float(input("What budget fits you (per person)?: "))

total_cost = (hotel_cost + food_budget + traveling_expense) * number_of_days
print(f"Total Cost: {total_cost}.")
cost_per_person = round(total_cost / number_of_people, 2)

if cost_per_person <= budget:
    print("This budget fits perfectly for you!")
else:
    print("Your budget exceeds! You need a better planning.")

print("Welcome to Smart Electricity Bill Generator!")

name = input("Enter your name: ")
city = input("Which city do you live?: ")
number_of_units = float(input("Enter the number of units consumed this month?: "))

meter_rent = 50

if number_of_units < 0:
    print("Invalid input!")
elif number_of_units <= 100:
    cost = number_of_units * 1.50
    status = "You are consuming low units!"
elif number_of_units <= 200:
    cost = number_of_units * 2.50
    status = "You are comsuming medium units!"
elif number_of_units <= 300:
    cost = number_of_units * 4.00
    status = "You are comsuming medium units!"
else: 
    cost = number_of_units * 6.00
    status = "You are comsuming high units!"

print(f"Name: {name}.")
print(f"City: {city}.")
print(f"Sub-Total: {cost}Rs.")
print(f"Tax: {cost * 0.16}Rs.")
print(f"Meter Cost: 50Rs.")
print(f"Final Cost: {cost + (cost * 0.16) + 50}Rs.")
print(status)

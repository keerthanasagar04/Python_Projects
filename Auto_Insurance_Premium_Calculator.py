driver_name = input("Driver's Name: ")
driver_age = int(input("Driver's Age: "))
years_licensed = int(input("How many years you had a driving license?: "))
accidents = int(input("Number of accidents from last 3 years: "))
vehicle_type = input("Vehical Type (sedan, suv, sports, truck): ").strip().lower()
vehicle_age = int(input("How old the car is in years: "))
annual_mileage = int(input("How many kilometers do you drive per year?: "))
has_multiple_policies = input("Do you already have another insurance policy with us? (True/False): ").strip().lower() == "true"
state_tier = int(input("Enter 1 for big city, 2 for town, and 3 for village: "))
driving_certificate = input("Have you completed a safe-driving course? (Yes/No): ").strip().lower()

# Rejections
if accidents >= 3:
    print("You cannot apply since you got more at-fault accidents.")
    exit()
elif years_licensed < 1:
    print("You must have license for more than 1 year.")
    exit()
elif driver_age < 21 and vehicle_type == "sports":
    print("You cannot have sports car when your age is under 21.")
    exit()

# Starting Price
if vehicle_type == "sedan":
    price = 8000
elif vehicle_type == "suv":
    price = 11000
elif vehicle_type == "sports":
    price = 18000
elif vehicle_type == "truck":
    price = 9500
else:
    print("Invalid Vehical Type!")
    exit()

base_price = price

# Young Drivers
if driver_age < 25 and years_licensed < 3:
    price += price * 0.35
elif driver_age < 25:
    price += price * 0.20

# Accidents
if accidents < 3:
    price += 1500 * accidents

# Vehicle Age                    
if vehicle_age > 10:
    price -= base_price * 0.10
elif vehicle_type == "sports" and vehicle_age <= 10:
    price += 2000

# Distance Driven 
if annual_mileage < 5000 and driver_age >= 25:
    price -= price * 0.05
elif annual_mileage > 20000:
    price += price * 0.08

# Other Discounts
if has_multiple_policies == True:
    price -= price * 0.10

if driving_certificate == "yes" and driver_age >= 25:
    price -= 500

# Location
if state_tier == 1:
    price += price * 0.12
elif state_tier == 3:
    price -= price * 0.06

price = round(price)
vehicle_type = vehicle_type.capitalize()

print("===== SecureDrive Insurance Quote =====")
print(f"Applicant: {driver_name}")
print(f"Vehicle: {vehicle_type}")
print(f"Final Premium: Rs.{price}")
print("=======================================")

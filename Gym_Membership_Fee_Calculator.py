name = input("Enter your name: ")
age = int(input("Enter your age: "))
membership_type = input("Membership type (1 for basic, 2 for premium, 3 for elite): ")
payment_frequency = input("Subscription (monthly/annual): ").lower()
has_referral = input("Did anyone refer you? (True/False): ").strip().lower() == "true"
city_tier = input("City Tier (1 (metro), 2 (tier-2 city), or 3 (small town)): ")

basic_fee = 1000
premium_fee = 2000
elite_fee = 3500

if membership_type == "1":
    fee = basic_fee
elif membership_type == "2":
    fee = premium_fee
elif membership_type == "3":
    fee = elite_fee
else:
    print("Invalid membership type.")
    exit()

if city_tier == "1":
    fee += 0
elif city_tier == "2":
    fee -= fee * 0.10
elif city_tier == "3":
    fee -= fee * 0.20
else:
    print("Invalid city tier.")
    exit()

if age < 18:
    if membership_type == "1":
        fee -= 200
    else:
        print("Members under 18 can only choose basic membership.")
        exit()
elif age >= 60:
    if membership_type != "3":
        fee -= fee * 0.15

if has_referral == True:
    if fee > 1500:
        fee -= 150
    else:
        fee -= 75

if payment_frequency == "annual":
    fee *= 12
    fee -= fee * 0.05
elif payment_frequency == "monthly":
    fee = fee
else:
    print("Invalid payment frequency")
    exit()

print("===== FitZone Membership Invoice =====")
print(f"Member: {name}")

if membership_type == "1":
    print("Membership: Basic")
elif membership_type == "2":
    print("Membership: Premium")
elif membership_type == "3":
    print("Membership: Elite")

payment_frequency = payment_frequency.capitalize()
print(f"Billing: {payment_frequency}")

print(f"Final Price: Rs.{round(fee, 2)}")
print("========================================")

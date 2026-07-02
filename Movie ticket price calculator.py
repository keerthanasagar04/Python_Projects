name = input("Enter your name: ")
age = int(input("Enter your age: "))
is_student = input("Are you a student (True/False)?: ").lower()
day = input("Day of booking ticket: ").lower()

base_price = 200

if age < 12:
    ticket_type = "Child"
    price = base_price - (base_price * 0.50)
elif age >= 60:
    ticket_type = "Senior"
    price = base_price - (base_price * 0.40)
else:
    if is_student == "true":
        ticket_type = "Adult (Student)"
        price = base_price - (base_price * 0.20)
    else:
        ticket_type = "Adult"
        price = base_price

if day == "monday":
    if price > 100:
        price = price - 50 

print("==== CineMax Ticket Receipt ====")
print(f"Customer: {name}")
print(f"Ticket Type: {ticket_type}")
print(f"Final Price: Rs.{price}")
print("================================")

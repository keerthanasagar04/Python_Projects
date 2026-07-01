print("Welcome to the bill calculator!")

name = input("Enter your name: ")

p1 = float(input("Price of first product: "))
q1 = int(input("Quantity of first product: "))

p2 = float(input("Price of second product: "))
q2 = int(input("Quantity of second product: "))

p3 = float(input("Price of third product: "))
q3 = int(input("Quantity of third product: "))

sub_total = (p1 * q1) + (p2 * q2) + (p3 * q3)
print(f"Sub total: {sub_total}")


if sub_total >= 200:
    discount = sub_total * 0.05
    print(f"Discount price: {discount}.")
    gst = (sub_total - discount) * 0.02
    print(f"GST: {gst}.")
    print(f"Final Price: {sub_total - discount + gst}")
else:
    gst = sub_total * 0.02
    print(f"GST: {gst}.")
    print(f"Final Price: {sub_total + gst}")

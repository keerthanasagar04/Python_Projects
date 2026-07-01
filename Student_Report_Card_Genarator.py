print("Welcome to Report Card Generator!")

student_name = input("Enter student name: ")
roll_number = input("Enter student roll number: ")

english_marks = float(input("What is your marks in English?: "))
hindi_marks = float(input("What is your marks in Hindi?: "))
math_marks = float(input("What is your marks in Math?: "))
science_marks = float(input("What is your marks in Science?: "))
social_marks = float(input("What is your marks in Social?: "))

print(f"Name: {student_name}")
print(f"Roll Number: {roll_number}")

total_marks = english_marks + hindi_marks + math_marks + science_marks + social_marks
print(f"Total Marks: {total_marks}.")

average = round(total_marks / 5, 2)
print(f"Average: {average}.")

percentage = round((total_marks / 500) * 100, 2)
print(f"Percentage: {percentage}%.")

if percentage >= 95:
    print("Grade: A")
elif percentage >= 85:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 55:
    print("Grade: D")
elif percentage >= 45:
    print("Grade: E")
else:
    print("Grade: F")

if percentage >= 45:
    print("Congratulations! You have passed in the exam! :)")
else:
    print("You have failed in the exam :(")


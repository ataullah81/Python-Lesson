# Ask for user input
name = input("What is your name? ")
score = int(input("What is your score? "))

print("Student: ", name)
print("Score: ", score)
# Check the condition
if score >= 90:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
else:
    print("Grade: C")
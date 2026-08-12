
'''
number = 1
while number <= 5:
    print(number)
    number +=1
#----------------------
number = 2
while number < 10:
    print(number)
    number += 2


# counting backward

number = 20
while number > 0:
    print(number)
    number -=1
print("Finished")
'''

password = input("Enter your password: ")

while password != "python123":
    print("Wrong password!")
    password = input("Try again: ")
print("Access granted!")

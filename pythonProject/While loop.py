
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

#-------------------------------

password = input("Enter your password: ")

while password != "python123":
    print("Wrong password!")
    password = input("Try again: ")
print("Access granted!")

#-----------------

password = input("Enter your password: ")

while password != "AI2026":
    print("Wrong password.")
    password = input("Try again: ")

print("Access granted!")

#----------------------------

for number in range(1, 8):
    print(number)

    if number == 4:
        break

print("Finished")

#-------------------------

for number in range(1, 8):
    #print(number)

    if number == 4: # skip 3 and print rest
    #if number % 2 !=0: # print even numbers because it skip the odd numbers
    #if number % 2 !=0: # print odd numbers because it skip the even numbers
        continue # skip iteration when number is = 3 and move to the next one
    print(number)

'''

for number in range(1,10):
    if number == 5:
        continue
    if number == 9:
        break
    print(number)
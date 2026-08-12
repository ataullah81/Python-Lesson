'''
for i in range(5):
    print(i)
'''
'''
range(stop)
range(start, stop)
range(start, stop, step)

But remember our rule: **the stop value is not included**.
'''
'''
# here 10 is start, 0 is stop and -2 is step in negative direction

for number in range(10, 0, -2):
    print(number)
    
#----------------------------------

for number in range(1,5):
    result = number * 3
    print(result)
#------------------------------------
total = 0
for number in range(1,7):
    if number % 2 == 0:
        total = total + number
print(total)

'''#------------------------
total = 0
for number in range (1, 7):
    if number % 2 != 0:
        total = total + number
print(total)
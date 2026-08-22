'''
numbers = [10, 25, 5, 40, 20]

print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(len(numbers))

# average

scores = [60, 70, 80, 90]
total = sum(scores)
count = len(scores)
average = total / count
print(average)

#combine with an if condition

scores = [60, 70, 80, 90]
average = sum(scores) / len(scores)

if average >= 70:
    print("Passed")
else:
    print("Failed")



#scores = [80, 90, 85, 95]
scores = [65, 80, 75, 90, 85]
average = sum(scores) / len(scores)
#total = sum(scores)
#count = len(scores)
#print(total)
#print(count)
print("Average:", average)
if average >= 90:
    print("Excellent")
elif average >= 70:
    print("Good")
else:
    print("Needs improvement")

#scores come from a loop

scores = [60, 75, 90, 85]
total = 0
for score in scores:
    total += score
print(total)


# Calculate sum and average
numbers = [10, 20, 30, 40]
total = 0
for number in numbers:
    total += number
average = total / len(numbers)
print("Total: ", total)
print("Average: ",average)

#counting without len()
scores = [70, 85, 90, 60]
count = 0
for score in scores:
    count += 1
print(count)

'''

#Conditional counting

scores = [55, 80, 65, 90, 75]

passed = 0
failed = 0
for score in scores:
    if score >= 70:
        passed += 1
    else:
        failed += 1
print("Passed: ", passed)
print("Failed: ", failed)
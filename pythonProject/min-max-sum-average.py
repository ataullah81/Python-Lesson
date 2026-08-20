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

'''

scores = [80, 90, 85, 95]

average = sum(scores) / len(scores)
total = sum(scores)
count = len(scores)
print(total)
print(count)
print(average)
if average >= 90:
    print("Excellent")
elif average >= 70:
    print("Good")
else:
    print("Needs improvement")


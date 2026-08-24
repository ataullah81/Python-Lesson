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


#calculate the percentage of students who passed

scores = [55, 80, 65, 90, 75]

passed = 0

for score in scores:
    if score >= 70:
        passed += 1
total_students = len(scores)

pass_percentage = passed / total_students * 100

print("Passed:",passed)
print("Total student:",total_students)
print("Paas percentage:",pass_percentage)

#---------------------------------
scores = [90, 45, 75, 60, 85, 95, 50, 70]

passed = 0
failed = 0

for score in scores:
    if score >= 70:
        passed += 1
    else:
        failed += 1

total_students = len(scores)
pass_percentage = passed / total_students * 100

print("Passed:", passed)
print("Failed:", failed)
print("Total:", total_students)
print("Pass percentage:", pass_percentage)

#---------------------------------
#finding values manually with a loop
scores = [60, 85, 70, 95, 80]
highest = scores[0]
for score in scores:
    if score > highest:
        highest = score
print(highest)

#---------------------------------

#Highest and lowest

scores = [70, 45, 90, 60, 85]

highest = scores[0]
lowest = scores[0]

for score in scores:
    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

print("Highest:", highest)
print("Lowest:", lowest)


#---------------------------------

# Score counter

scores = [85, 55, 70, 90, 65, 40]

high = 0
medium = 0
low = 0

for score in scores:
    if score >= 80:
        high += 1
    elif score >= 60:
        medium += 1
    else:
        low += 1
print("High:",high)
print("Medium:",medium)
print("Low",low)

#-------------------------------------------
#Create new list

scores = [85,55, 70, 90, 65, 40]

high_scores = []
medium_scores = []
low_scores = []

for score in scores:
    if score >= 80:
        high_scores.append(score)
    elif score >= 60:
        medium_scores.append(score)
    else:
        low_scores.append(score)
print("High:",high_scores)
print("Medium:",medium_scores)
print("Low:",low_scores)

#-------------------------------------------


#combine counting and storing

scores = [95, 50, 75, 82, 45, 88]

passed_scores = []

for score in scores:
    if score >= 70:
        passed_scores.append(score)
print("Passed scores:", passed_scores)
print("Number passed:",len(passed_scores))


#-----------------------------------------
#Calculating average passed scores

scores = [95, 50, 75, 82, 45, 88]

passed_scores = []

for score in scores:
    if score >= 70:
        passed_scores.append(score)
score_sum = sum(passed_scores)
average_passed =  score_sum / len(passed_scores)

print("Passed scores:", passed_scores)
print("Score sum:",score_sum)
print("Number passed:",len(passed_scores))
print("Average:",average_passed)



#ZeroDivistionError

scores = [40, 50, 35, 60]

passed_scores = []

for score in scores:
    if score >= 70:
        passed_scores.append(score)

if len(passed_scores) > 0:
    average_passed = sum(passed_scores) / len(passed_scores)
    print("Average",average_passed)
else:
    print("No student passed.")


#------------------------------

scores = [45, 80, 90, 55, 75]

passed_scores = []



for score in scores:
    if score >= 70:
        passed_scores.append(score)


print("Student passed:",len(passed_scores))
print("Passed score:", passed_scores)

if len(passed_scores) > 0:
    average = sum(passed_scores) / len(passed_scores)
    print("Average: ",average)
else:
    print("No student passed")
'''
#-----------------------------------
#Rounding decimal number

scores = [45, 80, 90, 55, 75]

passed_scores = []

for score in scores:
    if score >= 70:
        passed_scores.append(score)

if len(passed_scores) > 0:
    average = sum(passed_scores) / len(passed_scores)
    average = round(average, 2)

    print("Passed scores:", passed_scores)
    print("Students passed:", len(passed_scores))
    print("Average:", average)
else:
    print("No students passed.")
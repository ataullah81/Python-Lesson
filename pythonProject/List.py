'''
fruits = ["Apple","Banana","Mango"]
for fruit in fruits:
    print(fruit)


animals = ["Cat","Dog","Lion","Tiger"]
print(animals[3])

# Items append to the list
cars = ["Toyota", "BMW"]

cars.append("Volvo")
cars.append("Tesla")

print(cars)

# To print items one under another

animals = ["Cat","Dog","Lion","Tiger"]
for animal in animals:
    print(animal)



cars = ["Toyota", "BMW", "Volvo", "Tesla"]
cars.remove("BMW")
print(cars)

fruits = ["Apple", "Banana", "Mango", "Orange"]
fruits.pop(1)
print(fruits)


# remove item from the list and print removed item and remaining items
animals = ["Cat", "Dog", "Lion", "Tiger"]
removed_animals = animals.pop(2)
print(removed_animals)
print(animals)


# Length of a word
name = "Ataullah"
print(len(name))

# Length of a list
fruits = ["Apple", "Banana", "Mango"]
print(len(fruits))

animals = ["Cat", "Dog","Lion", "Tiger", "Wolf"]
animals.remove("Dog")
print(len(animals))


#checking whether something is in a list
animals = ["Cat", "Dog", "Lion"]
if "Tiger" in animals:
    print("Tigers found")
else:
    print("Tiger nor found!")
'''
#checking whether something is in a list, if not add that in the list
fruits = ["Apple", "Banana"]
if "Mango" not in fruits:
    fruits.append("Mango")
print(fruits)


#Slicing

fruits = ["Apple", "Banana", "Mango", "Orange", "Kiwi"]
print(fruits[1:4])

#Slicing
animals = ["Cat", "Dog", "Lion", "Tiger", "Wolf"]
print(animals[1:3])

#Slicing from beginning or to the end
animals = ["Cat", "Dog", "Lion", "Tiger", "Wolf"]
print(animals[:3])
print(animals[2:])
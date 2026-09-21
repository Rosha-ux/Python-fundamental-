# fruits = ["apple", "mango", "Pears"]

# for i in fruits:
#     print(i)



# for i in range(2,10,2):      #Range 
#     print(i)


# counting backwards

# for i in range(10, 0, -1):
#     print(i)



#Looping through strings

# name = "python"

# for letter in "python":
#     print(letter)


# Use else with for Loop

# for i in range(10):
#     print(i)

# else:
#     print("Loop finished")


# Enumerate using for loops

# fruits = ["Apple", "mango", "Pear"]

# for i, hero in enumerate(fruits, start = 1):
#     print(i, hero)


# Loop through multiple sequences:

names = ["John", "Sam", "Alex"]
ages = [20, 25, 30,24]

for name,age in zip(names, ages):
    print(name, age)
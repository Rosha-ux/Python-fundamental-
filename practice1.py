'''The user enters a string containing a number (e.g., ). Convert it to:Q4 "45"
• an integer
• a float
• a string again
Print all three values with their types.'''

user = str(input("number= "))

integer = int(user)

floating = float(user)

strings = str(user)


print(type(user))
print(type(integer))
print(type(floating))
print(type(strings))
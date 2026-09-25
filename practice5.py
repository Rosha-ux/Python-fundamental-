# Another conditional Statement example

age = int(input("Your age is: "))

if age < 12:
    print("This age belong to minor")

elif (age >= 12 and age <= 18):
    print("This age belong to Adolscene")

else:
    print("This age belong to Older")
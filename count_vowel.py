#Count the number of vowel word in given string:

word = "artificial_intelligence"

count = 0

for ro in word:
    if (ro == 'a' or
        ro == 'e' or
        ro == 'i' or
        ro == 'o' or
        ro == 'u'):
        count += 1
print("total number of vowel: ", count)


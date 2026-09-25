n= int(input("Given number: "))

num = n
total = 0
lod = len(str(n))

while num > 0:
    ld = num % 10
    total = total + (ld ** lod)
    num = num // 10

if total == n:
    print("given number is Armstrong")
else:
    print("not the Armstrong")

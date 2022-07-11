a = input("Enter a number: ")
sum = 0
for i in a:
    sum = sum + int(i)**3
if sum == int(a):
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")
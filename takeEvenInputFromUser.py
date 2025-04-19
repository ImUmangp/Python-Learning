#program takes input from user and checks if it is even or odd
# if it is even, it will print the number and ask for another number
# if it is odd, it will print the number and ask for another number

n=int(input("Enter a number: "))
if n%2==0:
    print("The number is even")
else:
    print("The number is odd")
while n%2==0:
    n=int(input("Enter a number: "))
    if n%2==0:
        print("The number is even")
    else:
        print("The number is odd")
while n%2!=0:
    n=int(input("Enter a number: "))
    if n%2==0:
        print("The number is even")
    else:
        print("The number is odd")
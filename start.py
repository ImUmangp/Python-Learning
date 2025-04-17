#print("Hello Bhai")

#name = input("Enter your name: ")
#print("Hello " + name + ", welcome to the world of Python!")

#a = 10
#b = 20
#if a > b:
 #   print("a is greater than b")
#elif a < b:
 #   print("a is less than b")
#else:
 #   print("a is equal to b")


#for printing numbers from 0 to 9
#for i in range(10):
 #   print("i:",i)

#for printing numbers from 0 to 9 with a comma and "anything" at the end
#for i in range(10):
 #   print(i, end=",grwee ")
#print()


#defining a function
#def add(a, b):
#    return a + b
#print(add(5, 10))

"""
#print even numbers from 0 to 10
def even_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=",")
    print()    

even_numbers(1, 10)
"""
"""
def odd_numbers(start,end):
    for i in range(start,end+1):
        if i%2 !=0:
            print(i,end=", ")
odd_numbers(1,10)

#Output:
#1, 3, 5, 7, 9,
"""

#Logic to hind comma at the end of the last number
def odd_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 != 0:
           if i + 2 > end:
                print(i, end="")
           else:
                print(i, end=",")
    print()
odd_numbers(1, 10)
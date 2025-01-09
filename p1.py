'''
Variables and Data Types
Basic Calculator: Write a program that takes two numbers from the user and performs addition, subtraction, multiplication, and division. Display the results.
Area of a Circle: Write a program that calculates and prints the area of a circle given its radius. Use the formula Area = π * radius^2.
'''

#Basic Calculator

print("Basic  Calculator")

yes = 'y'

while yes == 'y' or yes == 'yes' or yes=='ye' or yes == 'ys':
    a = float(input("\nEnter number 1: "))
    b = float(input("\nEnter number 2: "))
    r=0
    f=1
    while f==1:
        f=0
        c = input("\nSelect operation from(+,-,*,/): ")

        if c=='+':
             r = a+b
        elif c=='-':
            r=a-b
        elif c=='*':
            r=a*b
        elif c=='/':
            r=a/b
        else:
            print("\nPlease select operation from list[+,-,*,/]\n")
            f=1
    
    print("\nThe result is : ",r)
    yes = input("Enter yes to continue: ")
    

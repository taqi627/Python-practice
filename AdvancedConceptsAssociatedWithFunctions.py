##################
### {Recursion} ####
##################
import sys

sys.setrecursionlimit(1600)


def sum__to__n(n):
    if n == 1:
        return 1
    return n+sum__to__n(n-1)

result = sum__to__n(1500)

print(result)

###############################
####       {SCOPE}      #######
####        {and}       #######
#### {Nested Functions} #######
###############################


x= 50

def outer(y):


    def inner():
        global x
        x = 69
        y = 6

        print(f"x : {x} and y : {y}")
    inner()
outer(8)

print(f'globl x after modification : {x}')
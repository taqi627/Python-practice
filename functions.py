def intro(name,age):
    print(f'My name is {name} and my age is {age}')

intro('Taskeen',20)

add = lambda x,y:x+y

print(add(2,3))

def square(num=2):
    return num*num

sq1 = square()
print(sq1)
sq2 = square(7)
print(sq2)

sub = lambda x=6,y=4:x-y
print(sub(5))
print(sub)
print(sub(8,9))
print(sub(4,6))
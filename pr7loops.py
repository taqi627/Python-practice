for i in range(20):
    if i%2==1 :
        continue
    print(f'{i+1} ')

num = 999999999

if num <0 :
    num*=-1

print(num)
while num > 1:
    if num%2 == 0:
        num = num/2
    else :
        num= num*3+1

    print(num)

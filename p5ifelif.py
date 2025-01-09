num = 36

if num<0:
    print(f'{num} is negative')
elif num>0:
    print(f'{num} is possitive');
else:
    print(f'{num} is zero')

score = int(input('Enter your score : '))
print(score)
print()

if score >= 90 :
    print('A')
elif score >= 80:
    print('B')
elif score >= 70 :
    print('C')
elif score >=60:
    print('D')
elif score >= 50:
    print('D')
elif score >= 40:
    print('E')
else :
    print('F: fail')


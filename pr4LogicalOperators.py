import pr3ComparisonlOperators as cop

print('using logical operators with numbers : ')
print()

print(f'{cop.num1}<0 and {cop.num2}<0  : {cop.num1<0 and cop.num2<0}  ')
print()

print(f'{cop.num1}>0 and {cop.num2}<0  : {cop.num1>0 and cop.num2<0}  ')
print()

print(f'{cop.num1}>0 or {cop.num2}>0  : {cop.num1>0 or cop.num2>0}  ')
print()

print(f'{cop.num1}<0 or {cop.num2}>0  : {cop.num1<0 or cop.num2>0}  ')
print()

print(f' not { cop.num1}<0 and not { cop.num2}<0  : {not cop.num1<0 and not cop.num2<0}  ')
print()

print(f'not {cop.num1}>0 or not {cop.num2}>0  : {not cop.num1>0 or not cop.num2>0}  ')
print()
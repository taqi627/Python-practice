s1 = set([1,2,3,4,5,6])
s2 = set([1,3,7,11,17,27])

s3 = s1.union(s2)

print(s3)

s4 = s1.intersection(s2)
print(s4)

s5 = s3.difference(s4)

print(s5)

s6 = s3.symmetric_difference(s5)
print(s6)

list = [1,2,2,3,4,5,5,6,7,4,2,1,4,3,5,6,89,0,4,7,2,9,0,45,78,34,23,34,67,89,11]

s= set(list)

print(s)
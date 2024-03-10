s1 = {'a', 'b', 'c', 'd'}
s2 = {'c', 'e', 'b', 'f'}

print("s1 =", s1)
print("s2 =", s2)

s1.update(s2)

print(s1)

s3 = s1.union(s2)

print("s3 =", s3)

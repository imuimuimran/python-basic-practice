s1 = {'a', 'b', 'c', 'd'}
s2 = {'c', 'e', 'b', 'f'}

print("s1 =", s1)
print("s2 =", s2)

# s1.difference(s2)
# print(s1)

# s1.difference_update(s2)
# print(s1)

# s1.symmetric_difference(s2)
# print(s1)

s1.symmetric_difference_update(s2)
print(s1)
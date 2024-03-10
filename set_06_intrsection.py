s1 = {'a', 'b', 'c', 'd'}
s2 = {'c', 'e', 'b', 'f'}

print("s1 =", s1)
print("s2 =", s2)

# intersection remains only the elements of first set
s1.intersection(s2)
print("after intersection:", s1)

# intersection_update remains only the common elements of both set
s1.intersection_update(s2)
print("after intersection_update:", s1)
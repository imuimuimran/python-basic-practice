# Given three arrays, you have to find the common elements in three lists using sets.

ar1 = [20, 1, 80, 40, 10, 5]
ar2 = [100, 80, 6, 7, 20]
ar3 = [30, 70, 3, 15, 4, 120, 20, 80]

print("before sorting ar1 is:", ar1)
ar1.sort()
print("after sorting ar1 is:", ar1)

print("before sorting ar2 is:", ar2)
ar2.sort()
print("after sorting ar1 is:", ar2)

print("before sorting ar3 is:", ar3)
ar3.sort()
print("after sorting ar1 is:", ar2)

# Type casting from list into set
s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)

# join using intersection
s1s2 = s1.intersection(s2)
final_set = s1s2.intersection(s3)
print("The final common set is:", final_set)

# Type casting from set into list 
final_list = list(final_set)
print("The final common list is:", final_list)


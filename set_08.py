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

ar4 = set(ar1)
ar5 = set(ar2)
ar6 = set(ar3)

ar4.intersection_update(ar5)
print(ar4)

ar7 = ar4

ar7.intersection_update(ar6)
print(ar7)
print(type(ar7))

ar8 = list(ar7)

print(ar8)
print(type(ar8))


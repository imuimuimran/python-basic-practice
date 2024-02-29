'''
Operator	Example	    Meaning
and	        a and b	    Logical AND: True only if both the operands are True
or	        a or b	    Logical OR: True if at least one of the operands is True
not	        not a	    Logical NOT: True if the operand is False and vice-versa.

'''

exp1 = 2 > 1
exp2 = 5 < 3

print("exp1 and exp2 = ", exp1 and exp2)
print("exp1 or exp2 = ", exp1 or exp2)
print("not exp1 = ", not(exp1))
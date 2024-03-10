subjects = {'bangla', 'english', 'bangla', 'math'}

print(subjects)

# Add subjects
new_subjects = ["Chemistry", "Biology"]

subjects.update(new_subjects)

print(subjects)

# Remove Items
subjects.remove("bangla")
print(subjects)

# In remove() function if the mentioned item is not available, it show an error
# Instead of using femove() function, if we use discard function(), it does not show any error

sub = "Biology"
if sub in subjects:
    print(sub, "is in subjects list and after discard", sub, "the updated subjects are: ")
    subjects.discard(sub)
    print(subjects)
    
else:
    print(sub, "is not in subjects list. The subjects are mension below:")
    print(subjects)
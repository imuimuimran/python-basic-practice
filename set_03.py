subjects = {'bangla', 'english', 'bangla', 'math'}

for subject in subjects:
    print(subject)
    
print("Conditional print:")
for subject in subjects:
    if "la" in subject or "li" in subject: 
        print(subject)
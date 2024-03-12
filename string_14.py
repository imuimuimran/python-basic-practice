text = "the unexpected always happen"

print(text)
print(len(text))

if "pp" in text:
    print("pp is exist in the string")
else:
    print("pp in not exist in the string")
    
print(text[:11])

print(text.replace("always", "never"))

text2 = "no matter what"

new_text = text + " " + text2

print(new_text)
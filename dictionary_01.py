phones = {
    "Hasan" : 1712,
    "Masum" : 1912,
    "Mamun" : 1612
}

print(phones)

print(type(phones))

print(len(phones))

print(phones["Masum"]) #same thing can be done with the below line
print(phones.get("Masum"))

print(phones.keys())
print(phones.values())

# element in dictionary
phones["Hossain"] = 2345
print(phones)

new_number = {
    "Hossain" : 9876
}

phones.update(new_number)
print(phones)
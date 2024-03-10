phones = {
    "Hasan" : 1712,
    "Masum" : 1912,
    "Mamun" : 1612,
    "Hossain" : 2345
}

# print keys in dictionary
print("Print all keys: ")
for phone in phones:
    print(phone)
    
# print keys in dictionary
print("Print all keys another way: ")
print(phones.keys())

# print values in dictionary
print("Print all values: ")
for phone in phones:
    print(phones[phone])
    
# print values in dictionary
print("Print all values another way: ")
print(phones.values())

# print keys and values in dictionary
print("Print all keys and values: ")
for phone in phones.items():
    print(phone)
    
# print keys and values in dictionary
print("Print all keys and values another way: ")
for phones_keys, phones_values in phones.items():
    print(phones_keys, ":", phones_values)


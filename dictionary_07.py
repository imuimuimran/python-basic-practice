phones = {
    "Hasan" : 1712,
    "Masum" : 1912,
    "Mamun" : 1612,
    "Hossain" : 2345
}

print(phones)

# Remove items from dictionary
phones.pop("Masum")
print(phones)

# Remove the last item from the dictionary
phones.popitem()
print(phones)

# Clear all elements from dictionary
phones.clear()
print(phones)
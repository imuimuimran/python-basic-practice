phones = {
    "area1" : {
        "a" : 123,
        "b" : 132,
        "c" : 213  
    },
    "area2" : {
        "d" : 312,
        "e" : 321,
        "f" : 423
    }
}

print(phones)
print("area1: b:", phones["area1"]["b"])
print("area2: d:", phones["area2"]["d"])

print("area1: c:", phones["area1"]["c"])
phones["area1"]["c"] = 231 # update values
print("area1: c:", phones["area1"]["c"])
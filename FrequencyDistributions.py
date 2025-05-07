data = (2, 3, 4, 2, 5, 6, 3, 4)
Frequency= {}
for item in data:
    Frequency[item]= Frequency.get(item, 0) + 1
print("Frequency Distribution:")
for key in sorted(Frequency):
    print(f"{key}: {Frequency[key]}")
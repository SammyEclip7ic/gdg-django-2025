grades = {"John": "A", "Sara": "B", "Musa": "A"}
output = {}

for name, score in grades.items():
    if score in output:
        output[score].append(name)
    else:
        output[score] = [name]

print(output)

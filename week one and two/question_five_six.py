valid_numbers = []
total_sales = 0

with open("sales.txt", "r") as file:
    for line in file:
        try:
            line = int(line)
        except ValueError:
            pass
        else:
            valid_numbers.append(line)

for number in valid_numbers:
    total_sales += number

print(total_sales)
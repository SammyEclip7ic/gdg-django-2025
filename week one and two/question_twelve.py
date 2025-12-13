sum = 0
with open("numbers.txt", "r") as file:
    for number in file:
        try:
            number = int(number)
        except ValueError:
            pass
        else:
            sum += number

print(sum)

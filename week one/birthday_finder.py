from datetime import datetime

age = input("What is your age? ")
age = int(age)

birthyear = datetime.now().year - age
print(f"You were born on {birthyear}")

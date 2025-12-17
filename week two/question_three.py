with open("log.txt", "a") as file:
    file.write("User logged in\n")

with open("log.txt", "r") as file:
    contents = file.read()

print(contents)

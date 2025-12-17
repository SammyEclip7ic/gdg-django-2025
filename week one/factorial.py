def factorial_finder(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    
    print(result)

factorial_finder(3)

def sum_list():
    numbers = input("Enter a list of numbers, separated by spaces: ")
    numbers = numbers.split()
    sum = 0
    for num in numbers:
        sum += int(num)
    return sum
result = sum_list()
print(result)

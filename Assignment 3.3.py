def count_case(my_string):
    upper_count=0 
    lower_count=0
    for char in my_string:
        if char.isupper():
            upper_count += 1 
        elif char.islower():
            lower_count += 1
    return (upper_count, lower_count)

my_string=input("Enter a string: ")
result = count_case(my_string) 
print("No. of Upper case characters:", result[0]) 
print("No. of Lower case characters:", result[1])
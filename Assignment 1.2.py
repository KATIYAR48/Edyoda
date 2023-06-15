str = input("Input a string to reversed: ")

for char in range(len(str) - 1, -1, -1):
  print(str[char], end="")
print("\n")
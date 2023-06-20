ascii_atoz = {}
x=print
for i in range(ord('a'), ord('z')+1):
        ascii_atoz[chr(i)] = i
        # Printing the dictionary
x(ascii_atoz)
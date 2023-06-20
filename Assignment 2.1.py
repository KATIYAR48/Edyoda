x=print
sampl = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_tuples = sorted(sampl, key=lambda x: x[-1])
x(sorted_tuples)
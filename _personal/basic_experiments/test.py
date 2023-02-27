
# Original dictionary
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Use filter() to filter out odd values
filtered_dict = dict(filter(lambda x: x[1] % 2 == 0, d.items()))

print(filtered_dict)
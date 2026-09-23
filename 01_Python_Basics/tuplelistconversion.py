# Initial list of tuples
data = [
    ("A", 100),
    ("B", 200),
    ("C", 300)
]

# Convert list of tuples -> dictionary
result = {key: value for key, value in data}
print(result)

# Convert dictionary -> list of tuples
newdata = list(result.items())
print(newdata)

# Convert dict -> list of lists (comprehension)
listpairs = [[k, v] for k, v in result.items()]
print(listpairs)

# Convert dict -> list of lists (map)
list_pairs = list(map(list, result.items()))
print(list_pairs)

# Convert original tuple list -> list of lists
list2_pairs = [list(item) for item in data]
print(list2_pairs)

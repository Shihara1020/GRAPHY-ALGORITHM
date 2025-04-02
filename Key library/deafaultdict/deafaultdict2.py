from collections import defaultdict

d = defaultdict(list)  # Default value is []
d['a'].append(1)
d['a'].append(2)

print(d['a'])  # Output: [1, 2]
print(d['b'])  # Output: [] (default value)

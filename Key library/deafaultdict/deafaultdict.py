from collections import defaultdict

d = defaultdict(int)  # Default value is 0
print(d['a'])  # Output: 0

d['a'] += 1  # Now d['a'] = 1
print(d['a'])  # Output: 1

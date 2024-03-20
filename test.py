from collections import Counter

multi_set = Counter('aab')
other_set = Counter('abaa')

print(multi_set == other_set)
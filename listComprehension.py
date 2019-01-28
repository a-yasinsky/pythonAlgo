"""
list comprehansion
"""
[x for x in range(10) if x % 2 == 0]
# Out: [0, 2, 4, 6, 8]

[x if x % 2 == 0 else None for x in range(10)]
# Out: [0, None, 2, None, 4, None, 6, None, 8, None]

[x if x > 2 else '*' for x in range(10) if x % 2 == 0]
# Out: ['*', '*', 4, 6, 8]

[f(x) for x in range(1000) if f(x) > 10]
#use instead not ot calc f(x) twice
[v for v in (f(x) for x in range(1000)) if v > 10]

#dict
{x: x * x for x in (1, 2, 3, 4)}
swapped = {v: k for k, v in my_dict.items()}

# list comprehension
[x**2 for x in range(10)]
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#Python 2.x Version ≥ 2.4
# generator comprehension
(x**2 for x in xrange(10))
# Output: <generator object <genexpr> at 0x11b4b7c80

# Count the numbers in `range(1000)` that are even and contain the digit `9`:
print (sum(
1 for x in range(1000)
if x % 2 == 0 and
'9' in str(x)
))
# Out: 95

matrix = [[1,2,3],
[4,5,6],
[7,8,9]]
[[row[i] for row in matrix] for i in range(len(matrix))]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""
/list comprehension
"""

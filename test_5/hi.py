li = [1, 1, 2, 2, 3, 3, 5, 5, 5]

res = 0
for i in li:
    res ^= i   # XOR cancels out even occurrences

print("Number with odd occurrences:", res)



#Multiple odd-occurring numbers
#If there could be more than one, you can do this
# li = [1, 1, 2, 2, 3, 3, 5, 5, 5, 7, 7, 7]
# visited = set()  # to avoid rechecking same numbers
# for i in li:
#     if i not in visited:
#         if li.count(i) % 2 != 0:
#             print("Odd occurrence:", i)
#         visited.add(i)

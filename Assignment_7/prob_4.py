# n = 5
# start = 1
# for i in range(1, n + 1):
#     # Leading spaces (2 spaces for alignment)
#     print("  " * (n - i), end="")

#     # Increasing part
#     for j in range(start, start + i):
#         print(j, end=" ")

#     # Decreasing part
#     for j in range(start + i - 2, start - 1, -1):
#         print(j, end=" ")

#     print()
#     start += 1

for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end='')
    for j in range(1,i+1):
        print(j,end=' ')
    print('')            


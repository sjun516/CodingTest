# arr = [['A', 'B', 'V', 'D', 'E'], ['Y', 'X', 'Z', 'D', 'E']]
# arr = [['A', 'B', 'C', 'D', 'E']]

# print([row[:2] for row in arr])




# lst = [['A', 'B'], ['Y', 'X']]
# lst = [['A', 'B']]

# unique_alphabets = set()
# for row in lst:
#     for char in row:
#         print(char)
#         unique_alphabets.add(char)
# print(len(unique_alphabets))


m = 2048
arr = [-2048, 2048]

if m % 2 == 0 and -m in arr and m in arr:
    print(231)

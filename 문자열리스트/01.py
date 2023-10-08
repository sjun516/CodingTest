l = [['A', 'B', 'C', 'D', 'E'],
     ['F', 'G', 'C', 'O', 'E'],
     ['A', 'B', 'V', 'D', 'E'],
     ['Y', 'X', 'Z', 'D', 'E'],
     ['A', 'B', 'C', 'D', 'E']]#

length = len(l)
w = [1, 2, 4]
c = [2, 4]  # 수정된 c 리스트

arr = []
for i in range(len(w) + 1):
    if i == 0:
        arr.append(l[:w[i]])
    elif i == len(w):
        arr.append(l[w[i - 1]:])
    else:
        arr.append(l[w[i - 1]:w[i]])

print("행 슬라이싱 결과:")
print(arr)

arr2 = []
for array in arr:
    for i in range(len(c) + 1):
        if i == 0:
            arr2.append([row[:c[i]] for row in array])
        elif i == len(c):
            arr2.append([row[c[i - 1]:] for row in array])
        else:
            arr2.append([row[c[i - 1]:c[i]] for row in array])

print("열 슬라이싱 결과:")
print(arr2)


# 각 리스트에서 알파벳의 갯수를 세기 위한 함수
def count_alphabets(lst):
    alphabet_counts = {}
    for row in lst:
        for char in row:
            alphabet_counts[char] = alphabet_counts.get(char, 0) + 1
    return alphabet_counts

# 각 리스트에서 서로 다른 알파벳의 갯수를 세기 위한 함수
def count_unique_alphabets(lst):
    unique_alphabets = set()
    for row in lst:
        for char in row:
            unique_alphabets.add(char)
    return len(unique_alphabets)

# 각 리스트에서 서로 다른 알파벳 갯수 세기
unique_alphabets_counts = [count_unique_alphabets(sublist) for sublist in arr2]

# 가장 다양한 알파벳을 가진 리스트의 서로 다른 알파벳 개수 찾기
max_unique_alphabets_count = max(unique_alphabets_counts)
max_unique_alphabets_index = unique_alphabets_counts.index(max_unique_alphabets_count)

print("가장 다양한 알파벳을 가진 리스트의 서로 다른 알파벳 갯수:", max_unique_alphabets_count)





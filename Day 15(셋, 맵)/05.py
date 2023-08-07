# [필수] 도서관

N = int(input())
dic = {}
for _ in range(N):
	num = input()
	if(num in dic):
		dic[num] += 1
	else:
		dic[num] = 1
dic2 = dict(sorted(dic.items())) # 딕셔너리 키값정렬
result = 0
name = " "
for num in dic2:
	if dic2[num] > result:
		result = dic2[num]
		name = num
print(name)
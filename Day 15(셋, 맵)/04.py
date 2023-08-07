# 숫자카드뭉치

N = int(input())
dict = {}
arr = map(int, input().split())
for num in arr:
	if(num in dict):
		dict[num] += 1
	else:
		dict[num] = 1
		
M = int(input())
arr2 = map(int, input().split())
for num in arr2:
	if(num in dict):
		print(dict[num], end=" ")
	else:
		print(0, end=" ")
print()
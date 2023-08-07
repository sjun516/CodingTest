# 좌표 압축

N = int(input())
arr = list(map(int, input().split()))
sett = set()
for num in arr:
	sett.add(num)
	
arr2 = list(sett)
arr2.sort() 

dic = {}
for i in range(len(arr2)):
	dic[arr2[i]] = i
	
for num in arr:
	print(dic[num], end = " ")
print()
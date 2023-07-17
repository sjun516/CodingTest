# 화살표그리기_KOI전국2018_초등부_2
# 시간초과

num = int(input())
farray = []
sarray = []
distance = []

for i in range(num):
	a, b = map(int, input().split())
	farray.append(a)
	sarray.append(b)

for i in range(num):
	d = 0
	for j in range(num):
		if(sarray[i] == sarray[j] and i != j):
			if (d == 0 or abs(farray[i] - farray[j]) < d):
					d = abs(farray[i] - farray[j])
	distance.append(d)

result = 0
for i in range(num):
	result += distance[i]
print(result)
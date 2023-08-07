# 듣보잡

N, M = map(int, input().split())
arrN = set()
arrM = set()
for _ in range(N):
	arrN.add(input())
for _ in range(M):
	arrM.add(input())
	
print(len(arrN.intersection(arrM)))
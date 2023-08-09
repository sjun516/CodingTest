# [필수] 증가하는 가장 긴 수열 찾기

# O(N의 제곱)
N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)] # 수열 최대길이 저장 dp배열

for i in range(N): # N까지
	for j in range(i): # N보다 작은수까지
		if(arr[i] > arr[j]): # N과 앞의 N보다 작은수를 비교
			dp[i] = max(dp[i], dp[j]+1) # N보다 작은수를 찾으면 작은수의 dp배열과 원래있던 N의 dp배열 비교 

print(max(dp))


# O(Nlog(N))
import bisect

N = int(input())
LIS = [1 for _ in range(N)]
K = [0]
numbers = list(map(int, input().split()))

for i in range(N):
	X = numbers[i]
	LIS[i] = bisect.bisect_left(K, X)
	
	if LIS[i] == len(K):
		K.append(X)
	K[LIS[i]] = X

print(len(K) - 1)
# [필수] 수의 분할

# dynamic programming
x, n = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    for j in range(x):
        if i >= arr[j]:
            dp[i] += dp[i - arr[j]]

print(dp[n] % int(1e9 + 7))

# 재귀
import sys
sys.setrecursionlimit(10**7)

def case(n, arr, x):
    cnt = 0
    for i in range(x):
        if(n >= arr[i]):
            cnt += case(n-arr[i], arr, x)
    if(n == 0):
        return cnt + 1
    return cnt

x, n = map(int, input().split())
arr = list(map(int, input().split()))
print(case(n, arr, x))
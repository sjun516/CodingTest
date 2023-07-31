# [필수] 단지번호붙이기

num = int(input())
arr = [list(input()) for _ in range(num)]
chk = [[False for _ in range(num)] for _ in range(num)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    global cnt 
    
    if(x < 0 or y < 0 or x == num or y == num):
        return
    if(chk[x][y] == True):
        return
    if(arr[x][y] == "0"):
        return
    
    chk[x][y] = True
    cnt += 1
    
    for i in range(4):
        dfs(x + dx[i],y + dy[i])

ans = []
for i in range(num):
    for j in range(num):
        if(arr[i][j] == "1" and chk[i][j] == False):
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

# 출력
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
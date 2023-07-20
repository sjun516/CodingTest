# [필수] 조세퍼스 문제
# 리스트 보다는 큐모델을 사용하자

from collections import deque

def josephus(person, n):
    queue = deque(range(1, person + 1))
    arr2 = []

    num = 1
    while (len(queue) != 0):
        if num % n == 0:
            arr2.append(queue.popleft())
        else:
            queue.rotate(-1)  
        num += 1

    return arr2

person, n = map(int, input().split())
answer = josephus(person, n)
print(*answer)
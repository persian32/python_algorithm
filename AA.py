import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
res = 0  # 가장 많은 상금을 저장할 변수 (최댓값 갱신용)

for i in range(n):
    tmp = input().split()
    tmp.sort() # 정렬을 하면 조건 비교가 훨씬 쉬워집니다.
    a, b, c = map(int, tmp)
    
    # 상금 계산 로직 (조건문 패턴)
    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = c * 100 # sort했으므로 c가 가장 큰 눈입니다.

    # 패턴: 최댓값 갱신하기
    if money > res:
        res = money

print(res)
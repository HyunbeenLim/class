arr = ['A', 'B', 'C']
n = len(arr)

# 0x1을 쓰는 이유 - 비트 연산이라는 것을 명시(약속), 더 큰 진수를 쓰면 이진수로 표현하기 힘듦
def get_sub(tar):
    for i in range(n):
        if tar & 0x1:                   # 끝자리가 1로 끝나면 출력해라
            print(arr[i], end='')
        tar >>= 1                       # 한 자리 밀기

# tar = 0에서 7까지
## -> 000 001 010 011 100 101 110 111
for tar in range(0, 1 << n):  # range(0, 8)
    print('{', end='')
    get_sub(tar)
    print('}')
arr = 'ABCD'
N = len(arr)

def backtrack(k):
    if k == N:
        # 공집합 제거
        if A and B:
            print(A, B)
    else:
        # A에 포함시키기
        A.append(arr[k])
        backtrack(k + 1)
        A.pop()

        # B에 포함시키기
        B.append(arr[k])
        backtrack(k + 1)
        B.pop()

# 중복 제거
A, B = [arr[0]], []
backtrack(1)

'''
backtrack(0)이 아닌 backtrack(1)을 호출해서 리턴값이 2**N 개에서 2**(N-1)개로 줄어들었다!
반으로 줄어들었음 -> A에 arr[0]인 'A'를 포함시키면 알아서 중복이 제거된다!
'''
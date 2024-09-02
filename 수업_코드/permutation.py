# path = []

# def kfc(x):
#     # 1. 기저조건
#     # 0부터 시작, 3개를 뽑은 경우 종료
#     if x == 3:
#         print(path)
#         return
    
#     # 2. 후보군을 반복하면서
#     for i in range(1, 7):
#         # 2.1 재귀 호출 전에 경로를 기록
#         path.append(i)
#         # 2.2 다음 재귀 호출(파라미터 전달)
#         kfc(x + 1)
#         # 2.3 돌아왔을 때 - 사용했던 경로 삭제
#         path.pop()
        
# kfc(0)


# 중복을 취급하지 않는 순열 구현

# 전역 리스트를 사용(user or visited) - 이미 저장했던 숫자라면 continue

path = []
used = [0] * 7

# kfc 함수 그대로 가져와서 수정해보자
def kfc2(x):
    # 1. 기저조건
    # 0부터 시작, 3개를 뽑은 경우 종료
    if x == 3:
        print(path)
        return
    
    # 2. 후보군을 반복하면서
    for i in range(1, 7):
        # 방문했으면 넘어가라
        if used[i] == 1:
            continue
        # 2.1 재귀 호출 전에 경로를 기록, 사용도 기룍
        used[i] = 1
        path.append(i)
        # 2.2 다음 재귀 호출(파라미터 전달)
        kfc2(x + 1)
        # 2.3 돌아왔을 때 - 사용했던 경로 삭제 + 사용여부초기화
        path.pop()
        used[i] = 0
        
kfc2(0)
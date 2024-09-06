arr = ['A', 'B', 'C', 'D', 'E']
path = []
n = 3


def run(lev, start):
    if lev == n:
        print(*path)
        return

    for i in range(start, 5):
        path.append(arr[i])
        run(lev + 1, i + 1)             # lev - 몇개를 골랐는지 확인, i - 고른 숫자 기록
        path.pop()


run(0, 0)




# 주사위 던지기

dice = [1,2,3,4,5,6]
path = []
n = 3

def run(lev, start):
    if lev == n:
        print(*path)
        return
    
    for i in range(start, 6):
        path.append(dice[i])
        run(lev + 1, i)                 # 주사위 세개를 던지면, 중복을 허용하는 것 -> i로 해야 한다
        path.pop()

run(0,0)
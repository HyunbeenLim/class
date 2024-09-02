# 교안 주사위 눈금의 합
path = []


def kfc(x, sum):
    # 가지치기 - 이미 10을 넘는 경우의 수는 계산하지 말자
    if sum > 10:
        return

    # 기저조건: 3개를 던졌을 때 종료
    if x == 3:
        # 합이 10 이하인가요?
        if sum <= 10:
            print(f'{path} = {sum}')
        return

    # 후보군 탐색
    for i in range(1, 7):
        # i의 의미: 주사위 숫자
        path.append(i)
        kfc(x + 1, sum + i) # 주사위 결과를 더하여 전달
        path.pop()


kfc(0, 0)
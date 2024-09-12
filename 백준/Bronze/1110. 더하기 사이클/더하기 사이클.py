# N의 범위는 0 <= N <= 99
n = str(input())

# 10의 자리
first_text = 0
# 1의 자리
second_text = 0
# 반복 횟수
loop_count = 0
# 비교할 값
sum = ''

def split(a : str):
    global first_text
    global second_text
    
    if int(a) < 10:
        first_text = '0'
        second_text = a
    else:
        first_text = a[0]
        second_text = a[1]
        
split(n)
# 반복
while True:
    # 0이면 1을 반환
    loop_count += 1
    if n == '0':
        break
    
    first_text = int(first_text)
    second_text = int(second_text)
    # 첫번째 숫자와 두번째 숫자의 합산 값
    val = first_text + second_text
    # 10이 넘으면 Split
    if val >= 10:
        val = val % 10
    # 문자 상태로 합산
    sum = str(second_text) + str(val)
    # 루프
    if int(n) == int(sum):
        break
    else:
        split(sum)

print(loop_count)
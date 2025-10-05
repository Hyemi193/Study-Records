# ------------------------------------------------------------------------------------------------------
# 30.4 매개변수에 초깃값 지정하기
# ------------------------------------------------------------------------------------------------------
def personal_info(name, age, address = '비공개'):
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

personal_info('홍길동', 30)
personal_info('배트맨', 31, '서울시 용산구 이촌동')

# 30.4.1 초깃값이 지정된 매개변수의 위치
## 초깃값이 지정된 매개변수 다음에는 초깃값이 없는 매개변수가 올 수 없음
# def personal_info(name, address = '비공개', age):
#     print('이름 : ', name)
#     print('나이 : ', age)
#     print('주소 : ', address)

# def personal_info(name, age, address = '비공개'):
# def personal_info(name, age = 0, address = '비공개'):
# def personal_info(name = '비공개', age = 0, address = '비공개'):

# 심사문제 : 가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기
korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(korean, english, mathematics, science):
    
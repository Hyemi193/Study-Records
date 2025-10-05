# ------------------------------------------------------------------------------------------------------
# 29.4 함수에서 값을 여러 개 반환하기
# ------------------------------------------------------------------------------------------------------
# def add_sub(a, b):
#     return a + b, a - b

# x = add_sub(10, 20)
# print(x)    # 튜플이 반환

# def one_two():
#     return[1, 2]

# x, y = one_two()
# print(x, y)

# # ------------------------------------------------------------------------------------------------------
# # 29.5 함수의 호출 과정 알아보기
# # ------------------------------------------------------------------------------------------------------
# def mul(a, b):
#     c = a * b
#     return c

# def add(a, b):
#     c = a + b
#     print(c)
#     d = mul(a, b)
#     print(d)

# x = 10
# y = 20
# add(10, 20)

# # 심사문제 : 사칙 연산 함수 만들기
# x, y = map(int, input().split())

# def calc(x, y):
#     add = x + y
#     minus = x - y
#     multi = x * y
#     division = x / y
#     return add, minus, multi, division

# a, s, m, d = calc(x, y)
# print('덧셈 : {0}, 뺄셈 : {1}, 곱셈 : {2}, 나눗셈 : {3}'.format(a, s, m, d))

# ------------------------------------------------------------------------------------------------------
# Unit 30. 함수에서 위치 인수와 키워드 인수 사용하기
# ------------------------------------------------------------------------------------------------------
# 30.1 위치 인수와 리스트 언패킹 사용하기
# ------------------------------------------------------------------------------------------------------
## 위치 인수 : 함수에 인수를 순서대로 넣는 방식
# print(10, 20, 30)

# # 30.1.1 위치 인수를 사용하는 함수를 만들고 호출하기
# def print_numbers(a, b, c):
#     print(a)
#     print(b)
#     print(c)

# print_numbers(10, 20, 30)

# # 30.1.2 언패킹 사용하기
# x = [10, 20, 30]
# print_numbers(*x)
# print_numbers(*[10, 20, 30])

# # 30.1.3 가변 인수 함수 만들기
# def print_numbers(*args):
#     for arg in args:
#         print(arg)

# print_numbers(10)
# print_numbers(10, 20, 30, 40)

# x = [10]
# print_numbers(*x)

# y = [10, 20, 30, 40]
# print_numbers(*y)

# # 참고) 고정 인수와 가변 인수를 함께 사용하기
# def print_numbers(a, *arg):
#    print(a)
#    print(arg)

# print_numbers(1)
# print_numbers(1, 10, 20)
# print_numbers(*[10, 20, 30]) 

# ------------------------------------------------------------------------------------------------------
# 30.2 키워드 인수 사용하기
# ------------------------------------------------------------------------------------------------------
# def personal_info(name, age, address):
#    print('이름 : ', name)
#    print('나이 : ', age)
#    print('주소 : ', address)

# personal_info('홍길동', 30, '서울시 용산구 이촌동')
# personal_info(name = '이순신', age = 30, address = '대구시 달서구 상인동')
# personal_info(age = 20, address = '대구시 동구 신서동', name = '아이언맨')

# ------------------------------------------------------------------------------------------------------
# 30.3 키워드 인수와 딕셔너리 언패킹 사용하기
# ------------------------------------------------------------------------------------------------------
# def personal_info(name, age, address):
#    print('이름 : ', name)
#    print('나이 : ', age)
#    print('주소 : ', address)

# x = {'name' : '슈퍼맨', 'age' : 30, 'address' : '대구시 달서구 대천동'}
# personal_info(**x)
# personal_info(**{'name' : '슈퍼맨', 'age' : 30, 'address' : '대구시 달서구 대천동'})

# # 30.3.1 **를 두 번 사용하는 이유
# y = {'name' : '장보고', 'age' : 30, 'address' : '부산시 남구 남포동'}
# personal_info(*y)       # x의 키가 출력됨
# personal_info(**y)

# 30.3.2 키워드 인수를 사용하는 가변 인수 함수 만들기
def personal_info(**kwargs):
   for kw, arg in kwargs.items():
      print(kw, ' : ', arg, sep = '')

personal_info(name = '신사임당')
personal_info(name = '신사임당', age = 30, address = '서울시 용산구 이천동')

x = {'name' : '신사임당'}
personal_info(**x)

y = {'name' : '심사임당', 'age' : 30, 'address' : '대구시 달서구 진천동'}
personal_info(**y)

## 보통 *kwargs를 사용한 가변 인수 함수는 특정 키가 있는지 확인한 뒤 해당 기능을 만듬
def personal_info(**kwargs):
   if 'name' in kwargs:
      print('이름 : ', kwargs['name'])
   if 'age' in kwargs:
      print('나이 : ', kwargs['age'])
   if 'address' in kwargs:
      print('주소 : ', kwargs['address']) 

# 참고) 고정 인수와 가변 인수(키워드 인수)를 함께 사용하기
def personal_info(name, **kwargs):
   print(name)
   print(kwargs)

personal_info('홍길동')
personal_info('홍길동', age = 30, address = '서울시 용산구 이천동')
personal_info(**{'name' : '홍길동', 'age' : 30, 'address' : '서울시 용산구 이천동'})

# 참고) 위치 인수와 키워드 인수를 함께 사용하기
def custom_print(*args, **kwargs):
   print(*args, **kwargs)

custom_print(1, 2, 3, sep = ':', end = '')


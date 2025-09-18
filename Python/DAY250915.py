# ---------------------------------------------------------------
# Unit 8. 불과 비교, 논리 연산자 알아보기
# ---------------------------------------------------------------
# 8.1 불과 비교 연산자 사용하기
# ---------------------------------------------------------------
print(True); print(False)

# 8.1.1 비교 연산자의 판단 결과
print(3 > 1)

# 8.1.2 숫자가 같은지 다른지 비교하기
print('10과 10이 같다 :', 10 == 10); print('10과 5는 다르다', 10 != 5)

# 8.1.3 문자열이 같은지 다른지 비교하기
print('Python' == 'Python'); print('Python' == 'python'); print('Python' != 'python')

# 8.1.4 부등호 사용하기
print(10 > 20); print(10 < 20); print(10 >= 10); print(10 <= 10)

# 8.1.5 객체가 같은지 다른지 비교하기
print('구분', 1 == 1.0); print(1 is 1.0); print(1 is not 1.0)   # 1은 정수 객체, 1.0은 실수 객체이므로 두 객체는 서로 다름

# 참고) 정수 객체와 실수 객체가 서로 다름을 확인하는 방법
print(id(1), id(1.0))

# ---------------------------------------------------------------
# 8.2 논리 연산자 사용하기
# ---------------------------------------------------------------
print('구분')
# a and b
print(True and True); print(True and False); print(False and True); print(False and Flase)

# a or b
print(True or True); print(True or Flase); print(False or True); print(False or False)

# not x
print(not True); print(not False)

# not, and, or 순으로 판단
print(not True and False or not False)

# 8.2.1 논리 연산자와 비교 연산자를 함께 사용하기
print(10 == 10 and 10 != 5); print(10 > 5 or 10 < 3)
print(not 10 > 5); print(not 1 is 1.0)

# 참고) 정수, 실수, 문자열을 불로 만들기
print(bool(1)); print(bool(0)); print(bool(1.5)); print(bool('False'))

# 참고) 단락 평가
print(False and True); print(False and False)   # 첫 번째 값이 거짓이므로 두 번째 값은 확인하지 않고 거짓으로 결정
print(True or True); print(True or False)   # 첫 번째 값이 참이므로 두 번째 값은 확인하지 않고 참으로 결정
print(True and 'Python')
print('Python' and True); print('Python' and False)
print(False and 'Python'); print(0 and 'Python')
print(True or 'Python'); print('Python' or True)
print(False or 'Python'); print(0 or False)


# ---------------------------------------------------------------
# Unit 9. 문자열 사용하기
# ---------------------------------------------------------------
# 9.1 문자열 사용하기
# ---------------------------------------------------------------
hello = 'Hello, world!'
print(hello)
hello2 = '안녕하세요'
print(hello2)
hello3 = "Hello, world!"
print(hello3)
hello4 = '''Hello, Python!'''
print(hello4)
hello5 = """Python Programming"""
print(hello5)

# 9.1.1 여러 줄로 된 문자열 사용하기
hello = '''Hello, world!
안녕하세요.
Python입니다.'''
print(hello)

# 9.1.2 문자열 안에 작은따옴표나 큰따옴표 포함하기
s = "Python isn't difficult"
print(s)
s = 'He said "Python is easy"'
print(s)

single_quote = '''"안녕하세요."
'파이썬'입니다.'''
double_quote1 = """Hello
'Python'"""
print(single_quote)
print(double_quote1)

# 참고) 문자열에 따옴표를 포함하는 다른 방법
print('Python isn\'t difficult')

# 참고) 따옴표 세 개로 묶지 않고 여러 줄로 된 문자열 사용하기
print('Hello\nPython')


# ---------------------------------------------------------------
# Unit 10. 리스트와 튜플 사용하기
# ---------------------------------------------------------------
# 10.1 리스트 만들기
# ---------------------------------------------------------------
a = [38, 21, 53, 62, 19]
print(a)

# 10.1.1 리스트에 여러 가지 자료형 저장하기
person = ['james', 17, 175.3, True]
print(person)

# 10.1.2 빈 리스트 만들기
a = []
b = list()
print(a, b)

# 10.1.3 range를 사용하여 리스트 만들기
print(range(10))

a = list(range(10))
b = list(range(5, 12))
c = list(range(-4, 10, 2))
d = list(range(10, 0, -1))
print(a, b, c, d)
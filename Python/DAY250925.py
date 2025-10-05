# ------------------------------------------------------------------------------------------------------
# Unit 24. 문자열 응용
# ------------------------------------------------------------------------------------------------------
# 24.1 문자열 조작하기
# ------------------------------------------------------------------------------------------------------
# 24.1.1 문자열 바꾸기(.replace)
print('Hello, world!'.replace('world', 'Python'))

s = 'Hello, world!'
s = s.replace('world!', 'Python')
print(s)

# 24.1.2 문자 바꾸기(.translate)
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))

# 24.1.3 문자열 분리하기(.split)
print('apple pear grape pineapple orange'.split())

print('apple, pear, grape, pineapple, orange'.split(', '))

# 24.1.4 구분자 문자열과 문자열 리스트 연결(.join)
print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))

# 24.1.5 소문자를 대문자로 바꾸기(.upper)
print('python'.upper())

# 24.1.6 대문자를 소문자로 바꾸기(.lower)
print('PYTHON'.lower())

# 24.1.7 왼쪽 공백 삭제하기(.lstrip)
print('   Python   '.lstrip())

# 24.1.8 오른쪽 공백 삭제하기(.rstrip)
print('   Python   '.rstrip())

# 24.1.9 양쪽 공백 삭제하기(.strip)
print('   Python   '.strip())

# 24.1.10 왼쪽의 특정 문자 삭제하기
print(', python.'.lstrip(',.'))

# 24.1.11 오른쪽의 특정 문자 삭제하기
print(', python.'.rstrip(',.'))

# 24.1.12 양쪽의 특정 문자 삭제하기
print(', python.'.strip(',.'))

# 참고) 구두점 간단하게 삭제
import string
print(', python.'.strip(string.punctuation))            
print(string.punctuation)                               # 모든 구두점
print(', python.'.strip(string.punctuation + ' '))      # 공백까지 삭제
print(', python.'.strip(string.punctuation).strip())    # 메서드 체이닝

# 24.1.13 문자열 왼쪽 정렬(.ljust)
print('python'.ljust(10))

# 24.1.14 문자열 오른쪽 정렬(.rjust)
print('python'.rjust(10))

# 24.1.15 문자열 가운데 정렬(.center)
print('python'.center(10))
print('python'.center(11))

# 24.1.16 메서드 체이닝
## 메서드 체이닝 : 메서드를 줄줄이 연결하는 것
print('python'.rjust(10).upper())

# 24.1.17 문자열 왼쪽에 0 채우기
print('35'.zfill(4))
print('3.5'.zfill(6))
print('hello'.zfill(10))

# 24.1.18 문자열 위치 찾기(.find)
print('apple pineapple'.find('pl'))
print('apple pineapple'.find('xy'))

# 24.1.19 오른쪽에서부터 문자열 위치 찾기(.rfind)
print('apple pineapple'.rfind('pl'))
print('apple pineapple'.rfind('xy'))

# 24.1.20 문자열 위치 찾기(.index)
print('apple pineapple'.index('pl'))

# 24.1.21 오른쪽에서부터 문자열 위치 찾기(.rindex)
print('apple pineapple'.rindex('pl'))

# 24.1.22 문자열 개수 세기(.count)
print('apple pineapple'.count('pl'))
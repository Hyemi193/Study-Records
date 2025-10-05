# ------------------------------------------------------------------------------------------------------
# 24.2 문자열 서식 지정자와 포매팅 사용하기
# ------------------------------------------------------------------------------------------------------
# 24.2.1 서식 지정자로 문자열 넣기
print('I am %s.' % 'james')

name = 'maria'
print('I am %s.' % name)

# 24.2.2 서식 지정자로 숫자 넣기
print('I am %d years old.' % 20)

# 24.2.3 서식 지정자로 소수점 표현하기
print('%f' % 2.3)

## 소수점 자리 정하고 싶을 때
print('%.2f' % 2.3)
print('%.3f' % 2.3)

# 24.2.4 서식 지정자로 문자열 정리하기
print('%10s' % 'python')

# 참고) 자릿수가 다른 숫자 출력하기
print('%10d' % 150)
print('%10d' % 15000)

print('%10.2f' % 2.3)
print('%10.2f' % 2000.3)

## 왼쪽 정렬
print('%-10s' % 'python')

# 24.2.5 서식 지정자로 문자열 안에 값 여러 개 넣기
print('Today is %d %s.' % (3, 'April'))
print('Today is %d%s.' % (3, 'April'))

# 24.2.6 format 메서드 사용하기
print('Hello, {0}'.format('world'))
print('Hello, {0}'.format(100))

# 24.2.7 format 메서드로 값을 여러 개 넣기
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6))

# 24.2.8 format 메서드로 같은 값을 여러 개 넣기
print('{0} {0} {1} {1}'.format('Python', 'Script'))

# 24.2.9 format 메서드에서 인덱스 생략하기
print('Hello, {} {} {}'.format('Python', 'Script', 3.6))

# 24.2.10 format 메서드에서 인덱스 대신 이름 지정하기
print('Hello, {language} {version}'.format(language = 'Python', version = 3.6))

# 24.2.11 문자열 포매팅에 변수를 그대로 사용하기
language = 'User'
version = 3.6
print(f'Hello, {language} {version}')

# 참고) 중괄호 출력하기
print('{{{0}}}'.format('Python'))

# 24.2.12 format 메서드로 문자열 정렬하기
print('{0:<10}'.format('python'))       # 지정된 길이로 만든 뒤 왼쪽으로 정렬
print('{0:>10}'.format('python'))       # 지정된 길이로 만든 뒤 오른쪽으로 정렬
print('{:>10}'.format('python'))

# 24.2.13 숫자 개수 맞추기
print('%03d' % 1)
print('{0:03d}'.format(35))
print('%08.2f' % 3.6)
print('{0:09.2f}'.format(150.37))

# 24.2.14 채우기와 정렬을 조합해서 사용하기
print('{0:0<10}'.format(15))
print('{0:0>10}'.format(15))

print('{0:0>10.2f}'.format(15)) 

print('{0: >10}'.format(15))        # 공백으로 채우기  
print('{0:>10}'.format(15))         # 채우기 부분 생략시 공백이 들어감
print('{0:x>20}'.format(15))        # 남는 공간 문자 x로 채움

# 참고) 천단위로 콤마 넣기
print(format(1493500, ','))
print('%20s' % format(1493500, ','))
print('{0:,}'.format(1493500))

print('{0:>20,}'.format(1493500))
print('{0:0>20,}'.format(1493500))

# 심사문제 : 특정 단어 개수 세기
# s = input().split(" ")
# count = 0

# for i in s:
#     i = i.strip(',.!?;:"\'{}()[]')
#     if i == 'the':
#         count += 1
# print(count)

# 심사문제 : 높은 가격순으로 출력하기
# prices= map(int, input().split(';'))
# price = list(prices)
# price.sort(reverse = True)

# for num in price:
#     print('{0:>9,}'.format(num))

# ------------------------------------------------------------------------------------------------------
# Unit 25. 딕셔너리 응용
# ------------------------------------------------------------------------------------------------------
# 25.1 딕셔너리 조작
# ------------------------------------------------------------------------------------------------------
# 25.1.1 딕셔너리에 키-값 쌍 추가
## setdefault : 키-값 쌍 추가
## update : 키의 값 수정, 키가 없으면 키-값 쌍 추가

# 25.1.2 딕셔너리에 키와 기본값 저장
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
x.setdefault('e')
print(x)

x.setdefault('f', 100)
print(x)

# 25.1.3 딕셔너리에서 키의 값 수정
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}

# 키-값 수정
x.update(a = 90)
print(x)

# 키-값 쌍 추가
x.update(e = 50)
print(x)


x.update(a = 900, f = 60)
print(x)

## 키가 숫자일 경우
y = {1 : 'one', 2 : 'two'}
y.update({1 : 'ONE', 3 : "THREE"})
print(y)

y.update([[2, 'TWO'], [4, 'FOUR']])
print(y)

y.update(zip([1, 2], ['one', 'two']))
print(y)

# 참고) setdfault와 update의 차이
## setdefault : 키-값 쌍 추가만 가능
## update : 키-값 쌍 추가와 값 수정 모두 가능

# 25.1.4 딕셔너리에서 키-값 쌍 삭제(.pop)
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
x.pop('a')
print(x)

print(x.pop('z', 0))

x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
del x['a']
print(x)

# 25.1.5 딕셔너리에서 임의의 키-값 쌍 삭제(.popitem)
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
x.popitem()     # 파이썬 3.6 이상은 마지막 키-값 삭제
print(x)

# 25.1.6 딕셔너리의 모든 키-값 쌍 삭제(.clear)
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
x.clear()
print(x)

# 25.1.7 딕셔너리에서 키의 값 가져오기(.get)
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
print(x.get('a'))

print(x.get('z', 0))

# 25.1.8 딕셔너리에서 키-값 쌍 모두 가져오기
## items : 키-값 쌍을 모두 가져옴
## keys : 키를 모두 가져옴
## values : 값을 모두 가져옴
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
print(x.items())
print(x.keys())
print(x.values())

# 25.1.9 리스트와 튜플로 딕셔너리 만들기
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
print(x)

y = dict.fromkeys(keys, 100)
print(y)

# 참고) defaultdict 사용하기
from collections import defaultdict

y = defaultdict(int)

print(y['z'])
print(int())

z = defaultdict(lambda : 'Python')

print(z['a'])
print(z[0])

# ------------------------------------------------------------------------------------------------------
# 25.2 반복문으로 딕셔너리의 키-값 쌍을 모두 출력
# ------------------------------------------------------------------------------------------------------
x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
for i in x:
    print(i, end = ' ')
    print('')

## 키-값 모두 출력
for key, value in x.items():
    print(key, value)

for key, value in {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}.items():
    print(key, value)

# 25.2.1 딕셔너리의 키만 출력
for key in x.keys():
    print(f'키 =>', key, end = ' ')
print()

# 25.2.2 딕셔너리의 값만 출력
for value in x.values():
    print(f'값 =>', value, end = ' ')

# ------------------------------------------------------------------------------------------------------
# 25.3 딕셔너리 표현식 사용
# ------------------------------------------------------------------------------------------------------
keys = ['a', 'b', 'c', 'd']
x = {key : value for key, value in dict.fromkeys(keys).items()}
print(x)

print({key : 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()})
print({value : 0 for value in {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}.values()})
print({value : key for key, value in {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}.items()})

# 25.3.1 딕셔너리 표현식에서 if 조건문 사용
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# for key, value in x.items():
#     if value == 20:
#         del x[key]
# print(x)                          # ERROR : 딕셔너리는 for 반복문으로 반복하면서 키-값 쌍을 삭제하면 안됨

x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
x = {key : value for key, value in x.items() if value != 20}
print(x)

# ------------------------------------------------------------------------------------------------------
# 25.4 딕셔너리 안에서 딕셔너리 사용
# ------------------------------------------------------------------------------------------------------
terrestrial_planet = {
    'Mercury' : {
        'mean_radius' : 2439.7,
        'mass' : 3.3022E+23,
        'orbital_period' : 87.696
    },
    'Venus' : {
        'mean_radius' : 6051.8,
        'mass' : 4.8676E+24,
        'orbital_period' : 224.70069
    },
    'Earth' : {
        'mean_radius' : 6371.0,
        'mass' : 5.97219E+24,
        'orbital_period' : 365.25641
    },
    'Mars' : {
        'mean_radius' : 3389.5,
        'mass' : 6.4185E+23,
        'orbital_period' : 686.9600
    }
}

print(terrestrial_planet['Venus']['mean_radius'])

# ------------------------------------------------------------------------------------------------------
# 25.5 딕셔너리의 할당과 복사
# ------------------------------------------------------------------------------------------------------
x = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0}
y = x
print(x is y)
y['a'] = 99
print(x, y)

x = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0}
y = x.copy()
print(x is y)
print(x == y)
y['a'] = 99
print(x, y)

# 25.5.1 중첩 딕셔너리의 할당과 복사 알아보기
x = {'a' : {'python' : '2.7'}, 'b' : {'python' : '3.6'}}
y = x.copy()
y['a']['python'] = '2.7.15'
print(x, y)

d = {'a' : {'python' : '2.7'}, 'b' : {'python' : '3.6'}}
import copy
f = copy.deepcopy(d)
f['a']['python'] = '2.7.15'
print(d, f)

# 심사문제 : 딕셔너리에서 특정 값 삭제하기
keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

del x['delta']
x = {k : v for k, v in x.items() if v != 30}

print(x)
# ------------------------------------------------------------------------------------------------------
# Unit 24. 파일 사용하기
# ------------------------------------------------------------------------------------------------------
# 27.1 파일에 문자열 쓰기, 읽기
# ------------------------------------------------------------------------------------------------------
# # 27.1.1 파일에 문자열 쓰기
# file = open('hello.txt', 'w')
# file.write('Hello, world!')
# file.close()

# # 27.1.2 파일에서 문자열 읽기
# file = open('hello.txt', 'r')
# s = file.read()
# print(s)
# file.close()

# # 27.1.3 자동으로 파일 객체 닫기
# with open('hello.txt', 'r') as file:
#     s = file.read()
#     print(s)

# ------------------------------------------------------------------------------------------------------
# 27.2 문자열 여러 줄을 파일에 쓰기, 읽기
# ------------------------------------------------------------------------------------------------------
# # 27.2.1 반복문으로 문자열 여러 줄을 파일에 쓰기
# with open('hello.txt', 'w') as file:
#     for i in range(3):
#         file.write('Hello, world! {0}\n'.format(i))

# # 27.2.2 리스트에 들어있는 문자열을 파일에 쓰기
# lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

# with open('hello.txt', 'w') as file:
#     file.writelines(lines)

# with open('hello.txt', 'r') as file:
#     lines = file.readlines()
#     print(lines)

# # 27.2.4 파일의 내용을 한 줄씩 읽기
# with open('hello.txt', 'r') as file:
#     line = None
#     while line != '':
#         line = file.readline()
#         print(line.strip('\n'))

# # 27.2.5 for 반복문으로 파일의 내용을 줄 단위로 읽기
# with open('hello.txt', 'r') as file:
#     for line in file:
#         print(line.strip('\n'))

# ------------------------------------------------------------------------------------------------------
# 27.3 파이썬 객체를 파일에 저장하기, 가져오기
# ------------------------------------------------------------------------------------------------------
# 27.3.1 파이썬 객체를 파일에 저장하기
import pickle

# name = 'james'
# age = 17
# address = '서울시 서초구 반포동'
# score = {'korean' : 90, 'english' : 95, 'mathematics' : 85, 'science' : 82}

# with open('james.p', 'wb') as file:
#     pickle.dump(name, file)
#     pickle.dump(age, file)
#     pickle.dump(address, file)
#     pickle.dump(score, file)

# # 27.3.2 파일에서 파이썬 객체 읽기
# with open('james.p', 'rb') as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
#     address = pickle.load(file)
#     scores = pickle.load(file)

#     print(name)
#     print(age)
#     print(address)
#     print(scores)

# # 심사문제 : 특정 문자가 들어있는 단어 찾기
# with open('words.txt', 'r') as file:
#     for line in file:
#         words = line.replace(',', '').replace('.', '').split()
#         for word in words:
#             if 'c' in word:
#                 print(word)


# ------------------------------------------------------------------------------------------------------
# Unit 28. 회문 판별과 N-gram 만들기
# ------------------------------------------------------------------------------------------------------
# 28.1 회문 판별하기
# ------------------------------------------------------------------------------------------------------
# # 28.1.1 반복문으로 문자 검사하기
# word = input('단어를 입력하세요 : ')

# is_palindrome = True

# for i in range(len(word) // 2):
#     if word[i] != word[-1 -i]:
#         is_palindrome = False
#         break
# print(is_palindrome)

# # 28.1.2 시퀀스 뒤집기로 문자 검사하기
# word = input('단어를 입력하세요 : ')
# print(word == word[::-1])

# # 28.1.3 리스트와 reversed 사용하기
# word = 'level'
# print(list(word) == list(reversed(word)))

# # 28.1.4 문자열의 join 메서드와 reversed 사용하기
# word = 'level'
# print(word == ''.join(reversed(word)))

# ------------------------------------------------------------------------------------------------------
# 28.2 N-gram 만들기
# ------------------------------------------------------------------------------------------------------
# 28.2.1 반복문으로 N-gram 출력하기
# text = 'Hello'

# for i in range(len(text) - 1):
#     print(text[i], text[i + 1], sep = '')

# text2 = 'this is python script'
# words = text2.split()

# for i in range(len(words) -1):
#     print(words[i], words[i + 1])

# # 28.2.2 zip으로 2-gram 만들기
# text3 = 'hello'

# two_gram = zip(text3, text3[1:])
# for i in two_gram:
#     print(i[0], i[1], sep = '')

# text4 = 'this is python script'
# words = text4.split()
# print(list(zip(words, words[1:])))

# # 28.2.3 zip과 리스트 표현식으로 N-gram 만들기
# text = 'hello'
# print([text[i : ] for i in range(3)])
# print(list(zip(*['hello', 'ello', 'llo'])))
# print(list(zip(*[text[i:] for i in range(3)])))

# 심사문제 : 파일에서 회문인 단어 출력
with open('word.txt', 'r') as file:
    for word in file:
        word = word.strip('\n')
        if word == word[::-1]:
            print(word)

        
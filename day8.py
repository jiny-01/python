#내장함수
#파이썬에서 기본적으로 지원하는 함수(built-in function)

#abs()
#숫자의 절댓값을 리턴하는 함수
print(abs(10))
#all()
#all(x)는 반복 가능한 데이터(컬렉션) x를 입력값으로 받으면
#이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False 리턴
num_list = [1, 2, 0, 4]  #0은 False 이기 때문에 False 리턴
num_list = []
print(all(num_list))
print(all(num_list))
#any()
#얘는 그냥 all()의 반대 => 하나라도 참이면 True, 모두 거짓이면 False
num_list = [1, 2, 3, 4]
print(any(num_list))
num_list = [0, 0, 0, 0]
#chr()
#chr(i)는 유니코드를 넣으면 해당 문자로 리턴을 하는 함수
print(chr(97)) #a
print(chr(44032)) #가
#dir()
#객체가 지닌 변수나 함수를 보여주는 함수
name = "python"
print(dir(name))
num_list = [1, 2, 0, 4]
print(dir(num_list)) #.뒤에 쓸수 있는 함수 알려줌

#divmod()
#2개의 숫자 a, b를 입력받고 그리고 a를 b로 나눈 몫과 나머지를 튜플로 리턴
print(divmod(7,3)) #(2, 1) - (몫, 나머지)

#enumerate()
#순서가 있는 데이터(리스트, 튜플, 문자열)를 입력받아서 인덱스 값을 포함하는 객체를 리턴
a_list = ["name", "age", "birth"]
for i, name in enumerate(a_list):
    print(i, name)   #i: 인덱스번호, name: 값 ->

#eval()
#문자열로 구성되어 있는데 해당 문자열을 실행한 값
print(eval("1+2"))
print(eval("divmod(7,2)"))

#filter()
#첫 번째 인수로 함수, 두 번째 인수로 반복 가능한 데이터
#그리고 반복 가능한 데이터의 요소 순서대로 함수를 호출 했을 때
#리턴값이 참인 것만 묶어서 리턴

def positive(x):
    return x > 0

print(list(filter(positive, [1, -2, 5, -3, 8])))

#hex()
#정수를 입력받아 16진수 문자열로 변환하여 리턴하는 함수
print(hex(234))
print(hex(3))
#id()
#객체를 입력받아 고유 주솟값(레퍼런스)를 리턴하는 함수
a = 3
print(id(3))
#map()
#map은 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴
def two_time(x):
    return x*2

print(list(map(two_time, [1, 2, 3, 4]))) #x에 1,2,3,4 들어가서 x*2 한 값 리턴해서 리스트 형태로 출력

#max() / min()
#반복가능한 데이터 중에서 최대값 / 최솟값 리턴
num_list = [1, 3, 13, 20, 18, 17, 5, 9]
print(max(num_list))

#oct()
#oct()는 정수를 8진수 문자열로 바꾸어 리턴하는 함수
print(oct(34))
print(oct(12345))

#파일 여는 법
#open()
#open(filename, [mode])은 "파일 이름"과 "읽기 방법을
#입력받아 파일 객체를 리턴하는 함수 -> 파일을 여는 함수 (한글 파일명 가능)
# w 쓰기 모드
# r 읽기 모드
# a 추가 모드
# b 바이너리 모드

file = open("example.txt", "r", encoding="utf-8")  #한글로 인코딩하기 위해 encoding="utf-8" 필요
content = file.read()  #파일 읽기
print(content)
file.close() #꼭 닫아줘야함
# with 를 쓰면 close 를 따로 안 해줘도 됨
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()  # 파일 읽기
    print(content)

#ord()  <->  chr()
#ord()는 문자의 유니코드 숫자 값을 리턴하는 함수
print(ord("가"))
#chr(i)는 유니코드를 넣으면 해당 문자로 리턴을 하는 함수

#pow()
#첫 번째 인수의 두번째 인수만큼 거듭제곱한 값을 리턴하는 함수
print(pow(2, 4))

#range()
#range(시작, 끝, 간격)  for문과 함께 자주 사용
#이 함수는 입력받은 숫자에 해당하는 범위 값을
#반복 가능한 객체로 만들어 리턴
print(list(range(5, 100, 5)))  # -> 5개로 만들어줌

#round() : 반올림임
print(round(4.4))
print(round(8.9))
print(round(5.1234, 2))

#sum() : 합계
num_list = [1234, 582, 1475, 55752]
print(sum(num_list))












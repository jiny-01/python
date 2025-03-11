# #사용자정의 함수
# #def 함수이름():
# #   수행할 코드       #함수이름():호출
# #밑에서 함수 찾을 때는 Ctrl 누르면서 클릭하면 정의한 자리 찾아감
# from math import factorial
#
#
# #함수를 호출할 때 쓰는 매개변수
# #def 함수이름(매개변수1, 매개변수2..)
# #   수행할 코드   #함수이름(매개변수1, 매개변수2)
# #[return 반환값]
#
# #기본적인 사용자 정의 함수
# def func1():
#     print("Hello World")
#
# func1()
#
# def plus():
#     a = 2
#     b = 3
#     print(a + b)
#
# plus()
#
# #매개변수가 있는 사용자 정의 함수
# def hello(name="김지니"):
#     print(f"안녕하세요 저는 {name}입니다.")
#
# hello("김지니")
#
# def plus(x, y):
#     print(x + y)
#
# plus(5, 6)
#
# #def hello(name="김지니")   #hello(): 아무것도 없을 때 매개변수의 기본값 설정
#
# def introduce(name, age):
#     print(f"제 이름은 {name}이고 나이는 {age}입니다.")
#
# introduce("김지니", "25") #매개변수 여러 개일 땐 순서에 맞게 넣어야함
# introduce(name="김지니", age=25) #아니면 명시해주면 됨
#
# #리턴값이 있는 사용자 정의 함수
# def plus(x, y):
#     return x + y
#
# result = plus(1, 2)
# print(result)
# print(plus(1, 2))
#
# def multiple_seven(num):
#     return num * 7
#
# print(multiple_seven(3))
#
# def check_divide_seven(num):
#     if num % 7 == 0:
#         return True
#     else:
#         return False
#
# print(check_divide_seven(14))
# print(check_divide_seven(15))
#
# def factorial(num):
#     sum = 1
#
#     for n in range(num):
#         print(f"n = {n}")
#         sum = sum * (n + 1)
#         print(f"sum = {sum}")
#     return sum
#
# print(factorial(7))
#
# #평군 구하기
# def cal_average(scores):
#     sum = 0
#
#     for score in scores:
#         sum += score
#
#     return sum / len(scores) #len(): 요소의 개수
#
# score_list1 = [55, 70, 100]
# score_list2 = [100, 99, 88]
# score_list3 = [80, 70, 60]
#
# print(cal_average(score_list1))
# print(cal_average(score_list2))
# print(cal_average(score_list3))
#
# #콜백 함수
# #함수를 매개변수로 전달하여 필요할 때 호출하도록 하는 개념
# #어떤 함수가 실행되는 동안 미리 정의된 다른 함수를 호출하여 실행하는 역할
#
# def calculator(x, y, operation):
#     return operation(x, y)
#
# def plus(x, y):
#     return x + y
#
# def minus(x, y):
#     return x - y
#
# def multiple(x, y):
#     return x * y
#
# def divide(x, y):
#     return x / y
#
# print(calculator(4, 8, plus))  #plus() 가 아닌 plus 즉, 함수명만 적어라
# print(calculator(4, 8, minus))
# print(calculator(4, 8, multiple))
# print(calculator(4, 8, divide))
#
# import time
#
# # def timer(pause_second, callback):
# #     print(f"{pause_second}초 타이머가 시작되었습니다")
# #     print(f"{pause_second}초 뒤에 함수가 실행됩니다.")
# #
# #     time.sleep(pause_second)
# #
# #     callback()
# # print("타이머가 종료되었습니다.")
# #
# # def hello():
# #     print("안녕")
# #
# # timer(5, hello)
#
# #Lambda 함수(익명함수, 미지함수)
# #특정 범위 내에서만 사용되거나 호출되는 횟수가 한 번인 경우 매우 유용
# #Lambda  매개변수1, 매개변수2, ...: 함수 내부 코드
#
# def minus(x, y):
#     if x > y "양수" else "홀수"
#     return x - y
#
#
# print(plus(4, 5))
#
# add_lambda = lambda x, y: x + y
# print(add_lambda(4, 5))
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# double = list(map(lambda x: x * 2, numbers))
# print(double)
#
# map_result = map(lambda x: x * 2, numbers)
# list_result = list(map_result)
# print(list_result)
#
# parity = lambda x: "짝수" if x % 2 == 0 else "홀수"  #삼항 연산자
# print(parity(2))

#map, filter, 삼항연산자 많이 쓰임

#1. 두 수를 입력받고 두 수의 합을 출력하는 함수

# a = int(input("a를 입력하시오: "))
# b = int(input("b를 입력하시오: "))
#
# def plus(x, y):
#     print(x + y)
#
# plus(a, b)


#-------------------------------------------------------------------
#숫자 하나를 입력받고 해당 숫자가 짝수이면
#짝수를 출력하고 홀수이면 홀수를 출력하는 함수

num = int(input("a를 입력하시오: "))

def func(a):
    if a % 2 == 0:
        print("짝수")
    else:
        print("홀수")

func(num)






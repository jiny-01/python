#제어문
#명령어는 들여쓰기 안함, 수행할 문장은 들여쓰기함(tab 키 사용), 들여쓰기 취소: shift + tab
#조건문
# num = int(input("숫자를 입력해 주세요")) # input 으로 받는 것은 문자열 int 사용해서 형 변환
# if num > 0:
#     print("양수입니다.")
# else: print("음수입니다.")
#다중 조건문
# score = int(input("점수를 입력해 주세요:"))

#1번째 방법
# input_str = input("점수를 입력해 주세요.")
# if not input_str.isdigit():   #isdigit:숫자인지? -> 숫자가 아니면
#     print("숫자가 아닙니다.")
# else:
#     if int(input_str) >= 90:
#         print("A 입니다.")
#     elif int(input_str) >= 80:
#         print("B입니다.")
#     elif int(input_str) >= 70:
#         print("C입니다.")
#     else:
#         print("D입니다.")
# #2번째 방법
# if input_str.isdigit():
#     if int(input_str) >= 90:
#         print("A 입니다.")
#     elif int(input_str) >= 80:
#         print("B입니다.")
#     elif int(input_str) >= 70:
#         print("C입니다.")
#     else:
#         print("D입니다.")
# else: print("숫자가 아닙니다.")

# #숫자를 입력받고 짝수인지 홀수인지
# num = input("숫자를 입력해 주세요.")
# if num % 2 == 0:
#     print("짝수입니다")
# else:
#     print("홀수입니다.")

#test case 실습
#나이랑 학생인지 아닌지 두가지 질문 학생인지 아닌지에 대한 여부는 y/n, 18세 이상:성인
#만족하면: 성인이면서 학생이면 성인학생입니다.
#아니면: 성인학생이 아닙니다
# age = int(input("나이를 입력하세요"))
# student = input("학생입니까?(y/n)")
#
# if age >=18 and student == "y":
#     print("성인학생입니다.")
# else:
#     print("성인학생이 아닙니다.")

#반복문 - while
# num = 0
# while num < 10:
#     num += 1  #조건을 변경하는 코드
#     if num % 3 == 0:  #num 이 7이면 멈추기 -> if num == 7 break
#         continue      #3의 배수 건너뛰기 -> continue 해서 실행할 코드부터 실행 ->
#     print(num)

#구구단
# dan = 1
# while dan <= 9:
#     n = 1
#     while n <= 9:
#         print(f"{dan}x{n}={dan*n}")
#         n += 1
#     dan += 1

#5부터 5의 배수를 50 이하까지 조건
#근데 30 일 때 멈춤  if num == 30 break
#정답
# num = 5
# while num <= 50:
#     print(num)
#     if num == 30:
#         break
#     num += 5

#내가 한 거
# num = 5
# while num <= 50:     #중간중간 print(num) 찍어보기        print("1."+num) 처럼 구분하기
#     n = 1
#     print(f"{num}x{n}={num * n}")
#     if n <= 6:
#         break
#     n += 5

# for 문
# fruits = ["사과", "바나나", "체리", "딸기"]  #리스트
# for fruit in fruits:    #fruit는 지역변수이므로 for 문 밖에서 사용불가
#     print(fruit) #4개 들어있으므로 4번 반복
#
# score = {
#     "동윤": 80,
#     "종원": 70,
#     "지니": 100
# }
# for key in score:  #딕셔너리  #딕셔너리에서 key 는 지역변수? for 문 안에서 key
#     print(score[key])
#
#     print(f"{key}의 점수는 {score[key]}")
#
# a_tuple = ("안녕", "하세요", "반갑습니다") #튜플
# for a in a_tuple:
#     print(a)
#
# a_set = {3, 1, 1, 2, 4, 6, 2}  #세트
# print(sorted(a_set)) #sort: 원본을 정렬, #sorted: 정렬해서 리스트의 형태로 출력
# for a in sorted(a_set):
#     print(a)

# word = "python"  #문자열
# for i in word:
#     print(i)

# for i in range(1, 10):
#     print(i)
#     if i == 6:
#         break

# for i in range(1, 10):
#     print("1...", i)
#     if i == 5:         #5만 빼고 출력
#         continue
#     print("2...", i)
#
# for i in range(2, 101, 2): #2부터 100까지 짝수 출력
#     print(i)

#리스트 합 구하기
# total= 0
# num_list = [10, 20, 40, 60, 80]
# for i in num_list:
#     print(i)
#     total += i / length(num_list)
#     print("total:", i)

# print(total)

for num in range(1, 10):
    for n in range(1, 10):
        print(f"{num}x{n}={num* n}")


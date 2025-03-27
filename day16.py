# print(10 / 0)
# #ZeroDivisionError: division by zero 에서
# #에러 클래스 이름 ZeroDivisionError
# # division by zero: 에러 메시지

# num = int(input("숫자를 입력해주세요:"))
# print(10 / num)
#ValueError: invalid literal for int() with base 10: '안녕'
# #에러 클래스 이름 ValueError
# # invalid literal for int() with base 10: '안녕': 에러 메시지

###try-except
# try:
#     num = int(input("숫자를 입력해주세요:"))
#     print(10 / num)
# except:
#     print("예외발생!!")

###try-except [발생예외]
# try:
#         num = int(input("숫자를 입력해주세요:"))
#         print(10 / num)
# except ValueError:
#         print("문자말고 숫자 넣어라")
# except ZeroDivisionError:
#         print("0말고 딴 거 넣어라")



###try-except
# try:
#     my_list = [1, 2, 3]
#     index = int(input("리스트에서 가져올 인덱스: "))
#     print(my_list[index])
# except IndexError:
#     print("인덱스 범위가 아닙니다!!")
# except ValueError:
#     print("숫자만 입력하쇼")


###
# try:
#     with open("hi.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("파일 없음")


###try-else - finally
# try:
#     file = open("hi.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("파일 없음")
# finally:
#     file.close()   #예외 있든 없든 무조건 파일은 닫아야함

###try-except - else
# try:
#     num1 = int(input("숫자1: "))
#     num2 = int(input("숫자2: "))
#     result = num1 / num2
# except ValueError:             #숫자 아닌거 입력했을 때 에러
#     print("숫자만 입력하세요")
# except ZeroDivisionError:      #나누는 수가 0일 때 에러
#     print("0이상 숫자를 입력해주세요")
# else:
#     print(result)              #정상적일 때 실행될 코드


# ###
# try:                                  #에러 뜰 것 같은 부분
#     file = open("hello.txt", "r")
#     content = file.read()
# except FileNotFoundError:             #에러 뜬다면? 출력할 에러
#     print("파일이 존재하지 않습니다")
# else:                                 #에러 안 뜨고 정상적으로 실행될 부분
#     print(content)
# finally:
#     file.close()                      #에러 뜨든말든 파일은 무조건 닫아야하기 때문

#finally 는 무조건 마지막!!!!!#
#while 문 안에 try-except 넣어서 except 부분에 continue 사용하면 다시 실행되도록 할 수있음

BaseException

#예외처리 == 유효성검사

"""
Q. 리스트 요소 5개 선언하고 index 찾는 로직
-예외처리 하고 정상이면 해당 인덱스 값 출력  (예외처리: 해당 인덱스가 존재하지 않습니다. 출력)
-마지막은 항상 "끝!!" 출력
"""
#Q. 리스트 요소 5개 선언하고 index 찾는 로직
#예외처리 하고 정상이면 해당 인덱스 값 출력  (예외처리: 해당 인덱스가 존재하지 않습니다. 출력)
#마지막은 항상 "끝!!" 출력

# try:
#     list = [1, 2, 3, 4, 5]
#     index = int(input("리스트에서 인덱스 찾기: "))
#     print(list[index])
# except IndexError:
#     print("해당 인덱스가 존재하지 않습니다.")
# except ValueError:
#     print("숫자만 입력하시오.")
# else:
#     print(list[index])
# finally:
#     print("끝!!")

#==============================================================
#for 문 이용해서 리스트 개수만큼 반복
# list = [1, 2, 3, 4, 5]
# for i in range(len(list)):
#         try:
#             list = [1, 2, 3, 4, 5]
#             index = int(input("리스트에서 인덱스 찾기: "))
#             print(list[index])
#         except IndexError:
#             print("해당 인덱스가 존재하지 않습니다.")
#             continue
#         except ValueError:
#             print("숫자만 입력하시오.")
#         else:
#             print(list[index])
#         finally:
#             print("끝!!")

#강사님 풀이
# my_list = [1, 2, 3, 4, 5]
# try:
#     index = int(input("리스트에서 인덱스 찾기: "))
#     result = my_list[index]                   #try 문에서 에러 띄울 코드가 있어야함-> try 안에서 오류가 발생하도록
# except IndexError:
#         print("해당 인덱스가 존재하지 않습니다.")
# except ValueError:
#         print("숫자만 입력하시오.")
# else:
#         print(result)      #정상일 때 result 출력되도록
# finally:
#         print("끝!!")

"""
try 문에 에러 띄울 코드가 있어야함
"""
#try 문에 에러 띄울 코드가 있어야함


# ###커스텀 예외클래스 - > 예외 강제로 발생시키기
# # try:
# #     age = int(input("나이를 입력하세요 : "))
# #
# #     if age < 0 or age > 150:
# #         raise Exception("0이상 150미만 숫자만 입력해주세요")  #Exception 에러 띄우고, 메시지는 문자열
# # except Exception as e:          #e: 에러메시지
# #      print(e)
# # else:
# #      print(age)
# # finally:
# #      print("끝")

# ==================================================================
class AgeException(Exception):  # MyException: 자식 클래스 Exception: 부모클래스
        def __init__(self):
                super().__init__("0이상 150미만 숫자만 입력해주세요")     #AgeException 터지면 띄울 에러 메시지
#CTRL 누르면서 클래스(Exception) 들어가보면 이미 빌트인 된 클래스임을 알 수 있음

# try:
#     age = int(input("나이를 입력하세요 : "))
#
#     if age < 0 or age > 150:
#        raise AgeException()  # Exception 에러 띄우고, 메시지는 문자열
# except AgeException as e:    # e: 에러메시지
#     print(e)
# else:
#     print(age)
# finally:
#         print("끝")

#======================================================
#Q. 계좌 출금 시 잔액 부족할 때 에러발생
class FundsError(Exception):                #에러 클래스(계좌잔액<출금금액일때 에러) 만들기
    def __init__(self, balance, amount):
        super().__init__(f"출금 잔액 부족 현재 잔액 : {balance} / 출금 금액: {amount}")

class BankAccount():                        #출금계좌 클래스 만들기
    def __init__(self, balance):            #생성자: balance(계좌잔액)
        self.balance = balance

    def withdraw(self, amount):             #메소드: 출금액(amount) 출금하는 기능
        try:
            if amount > self.balance:       #계좌클래스의 객체이기 때문에(=내 계좌잔액) self.balance 로 해야함
                raise FundsError(self.balance, amount)
        except FundsError as e:
            print(e)
        else:
            self.balance - amount
            print(f"정상적으로 출금되었습니다. 남은 잔액: {self.balance - amount}")

account = BankAccount(100000)  #현재 계좌 잔액
account.withdraw(50000)        #메소드 - 출금액(amount) 호출


##숙제##
"""
Q1. 
my_dic = {1: "사과", 2: "바나나", 3: "딸기", 4: "포도", 5: "수박"}
-딕셔너리 키를 입력받음(숫자로) - input 이용
-result 변수에 해당 키의 값을 넣음  - 키에 해당하는 값을 넣음
-예외처리는 해당 키가 존재하지 않을 때 - keyerror "해당 키는 존재하지 않습니다" 출력
-그리고 숫자가 아닌 문자를 넣었을 때 - valueerror "숫자를 입력해 주세요"
-정상적으로 실행되면 해당 키의 값을 넣어둔 result 출력
-마지막은 항상 완료를 출력

"""

# my_dic = {1: "사과", 2: "바나나", 3: "딸기", 4: "포도", 5: "수박"}
# try:
#     key = int(input("키를 숫자로 입력하세요 : "))
#     result = my_dic[index]
#     if age < 0 or age > 150:
#        raise AgeException()  # Exception 에러 띄우고, 메시지는 문자열
# except AgeException as e:    # e: 에러메시지
#     print(e)
# else:
#     print(age)
# finally:
#         print("끝")




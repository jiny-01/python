#모듈화: 복잡한 프로그램을 작은 단위로 나누어 관리하고 개발하는 것

#모듈: 함수나 변수, 클래스를 모아 놓은 파이썬 파일
#모듈을 사용하는 이유
#-코드의 재사용성과 유지보수에 유용함
#코드의 가독성 향상

#표준모듈: 파이썬에서 기본적으로 제공하는 내장 모듈(빌트인 모듈)
#-별도의 설치 없이 import 문을 사용하여 바로 활용 가능

#주요 표준 모듈
#math : 수학 관련 모듈
#random: 난수(랜덤) 관련 모듈
#datetime : 날짜 및 시간 모듈
#json: json 데이터 처리 모듈
#re: 정규 표현식 모듈  -match 하여 맞는지 판정하는 모듈
#time: 시간, 타이머 모듈

#math
import math
#ceil - 올림
print(math.ceil(3.14))

#copysign - 두 번째 인자의 부호만 취해 첫 번째 인자에 적용
print(math.copysign(3.14, -1))

#fabs - 절댓값을 반환하는 메소드
print(math.fabs(-3.14))

#factorial - 팩토리얼 구하는 메소드
print(math.factorial(7))

#floor - 내림
print(math.floor(3.14))

#gcd - 두 수의 최대공약수
print(math.gcd(6, 8))

#modf - 정수 부분과 소수 부분을 분리해서 리턴
print(math.modf(3.14))  #->출력(0.1400000000012, 3.0)
#"부동소수점의 오류": 10진법 -> 2진법으로 바꾸는 과정에서 일어나는 오류(메모리에 저장되는 한계 때문)

#TRUNCATE - 내림
print(math.floor(-3.14)) #->  -4 무조건 아래로 내림
print(math.trunc(-3.14)) #->  -3 0으로 향해서 내림

#log(a, b) - b를 밑으로 하는 log a에 대한 로그 값
print(math.log(10, 10))

#원주율
print(math.pi)


#random 모듈
import random
#난수
print(random.random())

print(random.randint(1, 10)) #끝값 10도 범위에 포함
print(random.randrange(1, 10, 2)) #range: 끝값 포함 x, step(간격)옵션 가능

#shuffle : 순서를 랜덤하게 섞음
abc = ["a", "b", "C", "d", "e"]
random.shuffle(abc)
print(abc)

#choice
abc = ["a", "b", "C", "d", "e"]
print(random.choice(abc))

menu = "삼겹살", "된장찌개", "맥주", "소주"
print(random.choice(menu))

#datetime 모듈
from datetime import datetime, timedelta  #timedelta: 현재 날짜
#현재 날짜
now = datetime.now()
print(now)

one_week_later = now + timedelta(days=7)
print(one_week_later)

formatted_date = now.strftime("%Y%m%d %H:%M:%S")
print(formatted_date)

import os

print(os.getcwd()) #현재 디렉토리
print(os.listdir()) #현재 폴더의 파일 목록

if not os.path.exists("new_folder"):
    os.mkdir("new_folder")  #mkdir: make directory 디렉토리 만드는 것

#정규표현식 모듈
import re

pattern - r"[a-za-Z0-9.-+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}"

pattern = r"\d{3}-\d{4}-\d{4}"
phone_namber = 010-1234-5678

if re.match(pattern, phone_namber):
    print("올바른 전화번호")
























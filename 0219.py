# print("Hello World")
#
# name = "김지니"
# age = 25
#
#
# "제 이름은 ____ 입니다."
# print("제 이름은" + name + "입니다.") #띄어쓰기 X
# print("제 이름은", name, "입니다.") #띄어쓰기 0
# "제 나이는 __ 입니다."
# print("제 나이는", age, "입니다.")  #age는 숫자형
# print("제 나이는 {} 이고 이름은 {} 입니다.".format(age, name))  #{}: 변수값이 들어갈 자리를 표시, .format(): 중괄호 안에 들어갈 변수
# print("제 나이는 {a} 이고 이름은 {b} 입니다.".format(a=25, b="김지니"))
# print(f"제 나이는 {age} 이고 이름은 {name} 입니다.") # 문자열 앞에 f 써주면 바로 변수 입력 가능 -> f string 방식
# print("제 나이는 %s 입니다." % age) # %s: 자리에 age을 문자열로 바꿔서 넣겠다. -> % string 방식
# print("제 나이는 %d 입니다." % age) # %d: 모든 숫자를 정수형으로 바꿔서 넣는 것
# print(f"제 나이는 %d 이고 이름은 %s 입니다." % (age, name))
# print("제 지분은 %d %% 입니다." % 2)
#
# first_name = "지니"
# last_name = "김"
# height = 164
#
# print("제 이름은 {} 이고 성은 {} 이며 키는 {} 입니다. ".format(first_name, last_name, height))
# print(f"제 이름은 {first_name} 이고 성은 {last_name} 이며 키는 {height} 입니다.")
#
# print("%10.2f" %3.141565153) # .n: 소숫점 n번째 자리까지만 출력, 0: 몇 자리인지 상관없다, 정수부분: n자리로 출력하란 의미
# print("%10.3f" % 3.141565153) #%"자릿수"."몇번째소수점"f  #Q. 출력할 때 반올림된 결과값 출력?
#
# #입력
# #input()
# email = input("이메일 : ")
# hobby = input("취미 : ")
# address = input("주소 : ")
# age = int(float(input("나이 : "))) #int: 정수형으로 바꿈, float: 실수형으로 바꿈
# #형 변환 : input의 문자열을 먼저 float 로 실수형으로 바꾼 후, int 로 정수형으로 변환 int()에는 실수형을 넣어야함
#
# #print("제 이메일은 {a} 이고 취미는 {b} 이며 주소는 {c}입니다.".format(a=email, b=hobby, c=address))
#
# print(f"제 이메일은 {email}, 제 취미는 {hobby}, 나이는 {age}") # int함수로 age 를 정수형으로 바꿈
#
# #문자열의 인덱싱: 번호(=인덱스)를 부여 (0부터~), 역순: 뒤에서부터 -(음수로), -1부터
#
# a = "Life is too short, You need Python"
# print(a[10])  # e 출력, [] 안에 숫자 넣어줌
# #문자열의 슬라이싱  문자열[start:end:step] 시작, 끝, 간격으로 추출/ end: 자기 포함안하고 자기 앞 번호까지만(7번째까지만)
# #[::2] : 번호 없으면 처음부터 끝까지 2칸씩 출력

# date = "20250218sunny"
# date2 = "20260505cloudy"
#
# #연도, 월, 일, 날씨
# #연도는 2025, 월은 02 일은 18 날씨는 sunny  출력해보기
#
# year = date[0:4]
# month = date[4:6]
# day = date[6:8]
# weather = date[8:14]

# #print(f"연도는 {}, 월은 {(date[4:6])}, 일은 {}. 날씨는 {}")
# print(f"연도는 {date[0:4]}, 월은 {date[4:6]}, 일은 {date[6:8]}. 날씨는 {date[8:13]}")
# print(f"연도는 {date2[0:4]}, 월은 {date2[4:6]}, 일은 {date2[6:8]}. 날씨는 {date2[8:]}")
# #print(f"연도는 {year}, 월은 {month}, 일은 {day}, 날씨는 {weather}")

# 다양한 문자열 함수: index, strip(공백 제거), find, join, count, replace, split
#a = "Life is too short, You need Python"
#print(len(a)) # 문자열 길이
# print(a.count("t", __start:5,__end:10)) # 문자가 몇 개 있는지

# print(a.index("t")) #앞에서부터 찾는데 해당 문자의 인덱스 번호를 찾아줌  #띄워쓰기도 인덱스포함
#####index 는 해당 문자가 없으면 오류를 낸다. - 여기서 종료됨 #####
# print(a.find("X"))
# #find : 없어도 오류는 안 나지만 없으면 -1 출력함, 문자열에서만 사용 가능
# print(a.lower()) #upper, lower: 소문자/대문자로 바꿈
#print(a[0].isupper()) #True, False 로 출력
# print(a.replace("short", "long")) # replace(old, new) 결과값만 바뀌어서 출력함 (원래 문장은 안 바뀜)
# print(a)
# print(a.replace(" ", ""))
# print(a.strip()) #strip(): 문자열 내 공백제거, lstrip:왼쪽 공백 제거, rstrip:오른쪽 공백 제거
# print(a.split()) # 공백, tab 등 기준으로 나뉘어져서 출력 -> list(배열) 의 형태로 반환
# b = "a:b:c"
# print(b.split(":"))

email = input("email : ") #allie7019@naver.com 에서 id 만 출력하기
#id 는 allie7019, 슬라이싱을 해야함, @인덱스를 구하는 함수를 이용, -> 알고리즘

print(email.index("@"))
email_id = (email[0:email.index("@")])
print(f"id는 {email_id}") 
 #앞에서부터 찾는데 해당문자의 인덱스 번호를 찾아줌


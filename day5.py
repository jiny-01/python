#연산자: 변수나 값을 연산하는 기호
# x = 10 #대입
# x += 10 #더하고 대입(할당)
# x *= 3 #곱하고 대입(할당) x = x * 3
# x /= 2  #/: 실수형 , //: 정수몫 x = x / 2
# x //= 2 # 나누고(몫이 정수) x = x // 2
# print(x)
x = 10
y = 20
z = 10
print(x == z) #같다
print(x != z) #같지 않다
print(x > y) #왼쪽 기준 오른쪽보다 크다. - False
print(x > z)
print(x >= z) #크거나 같다
print(x <= y) #작거나 같다
#논리연산자
a = True
b = False
print(a and b) #True
print(a or b) #True
print(not a) # False
print(not a and b) #not a = False 이므로 False and False 이기에 False 출력
#조건연산자 (삼항연산자)
# a = 10
# b = 20
# max_value = a if a > b else b
# print(max_value)
# if a > b:
#     max_value = a
# else:
#     max_value = b
#




score = 85
grade = "A" if score >= 90 else("B" if score >= 80 else "C")
#90점 이상일 때 A, 80점 이상일 때 B, 그 외 C
print(grade)
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")


answer = 25
number = int(input("1부터 50까지의 수 중 하나를 입력하세요: "))
print(number)

# if number == answer:
#     print("정답입니다.")
# else: print("다시 시도하세요")

while number != answer:
    number = int(input("숫자를 입력하세요: "))
    if number == answer:
        print("정답입니다.")
    elif number > answer:
        print("down")
    else:
        print("up")




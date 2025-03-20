from mypackage2.review.review import review
from mypackage2.study.study import study

#공부하기 함수 정의
#review_list(객체) 를 review_file(저장) 로 저장
                                                                               #indent 들여쓰기 4칸, 아스키코드=false 로 깨끗하게 출력

#오답노트(=리뷰함수) 불러오는 함수


while True:
    print("=========메뉴=========")
    print("""
        1. 초등
        2. 중고
        3. 전문
        4. 오답노트
    """)

    #메뉴선택하기
    choice = input("메뉴를 선택하세요 : ")
    if choice == "1":
        study("초등")
    elif choice == "2":
        study("중고")
    elif choice == "3":
        study("전문")
    elif choice == "4":
        review()
    elif choice == "5":
        break

    else:
        print("다시 선택해 주세요.")
        continue





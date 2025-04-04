import json
import random

def study(level):
    review_list = []  #오답노트 만들기 위한 리스트

#난이도 "level" filter 이용해서 "초급"인 값만 출력해서 list 형태로 저장
    with open("../words.json", "r", encoding="utf-8") as file:
        word_list = list(json.load(file))  #json 모듈의 메소드를 쓰기 위함, json 파일 데이터 가져옴
        filtered_word_list = list(filter(lambda x: x["level"] == level, word_list))
        print(filtered_word_list)

        count = 0
        #review_list = [] 여기 있어도 상관은 없음

        while count < 10: #랜덤으로 10번
            select_index = random.randint(0, len(filtered_word_list))   #랜덤의 범위(0, 레벨별 단어 개수만큼)
            print("========================")                          #딕셔너리들의 집합으로 만들어진 리스트에서
            print(f"{filtered_word_list[select_index]["meaning"]}")    #key 가 "level" 인 값이 level 인 숫자 개수("초급"인 숫자 개수)

            # a = filtered_word_list[select_index]
            # b = a["meaning"]
            # print(f"{b}")

            input_eng = input("단어 : ")
            if input_eng == filtered_word_list[select_index]["word"]:
                print("정답입니다!!!")
            elif input_eng != filtered_word_list[select_index]["word"]:
                print("오답입니다!!!")
                print(f"정답 : {filtered_word_list[select_index]["word"]}")
                review_list.append(filtered_word_list[select_index])

            count += 1

        with open("../review_note.json", "w", encoding="utf-8") as review_file:
            json.dump(review_list, review_file, indent=4, ensure_ascii=False)
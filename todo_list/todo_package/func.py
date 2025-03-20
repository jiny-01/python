#todo_list 에서 쓸 모듈

import json

def save_todo(todo_list):      #여기의 todo_list 는 매개변수
    with open("../todo.json", "w", encoding="utf-8") as file:
        json.dump(todo_list, file, indent=4, ensure_ascii=False)

    print("저장되었습니다!")

#아래의 todo_list 와 save 함수의 todo_list 는 다른 것임

##1. 할 일 추가 함수
def add():
    todo_list = []
    while True:
        todo_name = input("할 일(그만하려면 종료 입력) : ")
        todo_complete = False
        if todo_name == "종료":
            save_todo(todo_list)
            break

        todo_list.append(
            {
                "todo_name" : todo_name,
                "todo_complete" : todo_complete
            })


##2. 할 일 조회하는 함수
def check():
    with open("../todo.json", "r", encoding="utf-8") as file:
        todo_list = list(json.load(file))

    for i in range(0, len(todo_list)):
        # print("요소 : ", todo_list[i])
        # print("값 접근 : ", todo_list["todo_name"])
        print(f"{i + 1}. 할 일 : {todo_list[i]["todo_name"]}")                #todo = todo_list[i]
        print(f"완료 상태 : {"완료" if todo_list[i]["todo_complete"] else "미완료"}")                                                                         #todo_name = todo_list["todo_name"]

    return todo_list


##3. 할 일 수정하는 함수
def update():
    todo_list = check()   #check 함수를 써서 json 파일을 불러옴(저장된 것 열기)
    while True:
        choice_todo = int(input("몇 번째 Todo?"))
        todo = todo_list[choice_todo - 1]

        todo["todo_name"] = input("할 일 수정 : ")
        choice_complete = input("할 일 완료(y/n) : ")

        if choice_complete == "y":
            todo["todo_complete"] = True
        elif choice_complete == "n":
            todo["todo_complete"] = False
        continue_choice = input("또 수정하시겠습니까?(y/n)")
        if continue_choice == "y":
            continue
        elif continue_choice == "n":
            save_todo(todo_list)
            break



##4. 할 일 삭제하는 함수
def delete():
    todo_list = check() #불러오기
    if len(todo_list) == 0:   #todo_list 가 0 개일 때
        print("삭제할 게 없음")
    else:
        choice_todo = int(input("몇 번째 할 일을 삭제할 거?"))
        del todo_list[choice_todo - 1]

    save_todo(todo_list)

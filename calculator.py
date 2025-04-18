import tkinter as tk

#새 창 만들기
root = tk.Tk()
root.title("계산기")

#계산기 입력창
cal_entry = tk.Entry(root, width = 50)
cal_entry.grid(row=0, column=0, columnspan=4)

#숫자 버튼 시 수행될 메소드
def btn_click(value):
    cal_entry.insert(tk.END, str(value))

#value => for 문에서 언패킹했던(람다에 쓴 i의 값)

#clear 버튼 메소드
def clear_all():
    cal_entry.delete(0, tk.END)

#=버튼 메소드
def calculate_result():
    content = cal_entry.get()    #entry 에 입력된 값 가져오기
    if "/" in content:                #입력값에 /가 있을 경우
        result = int(eval(content))   #결과값은 정수로 변환
    else:
        result = eval(content)           #결과에 계산된 값 출력하기
    cal_entry.delete(0, tk.END)  #연산과정 지워지게
    cal_entry.insert(tk.END, str(result))  #숫자와 연산자가 섞여있음  #내장함수

    #예외처리 - 45+  처럼 수식이 안 끝났을 때 에러 띄우기


#DEL 버튼 메소드 - 하나씩 지우기
def remove():
    content = cal_entry.get()
    if content:
        new_content = content[:-1]
        cal_entry.delete(0, tk.END)
        cal_entry.insert(0, new_content)



#============================버튼 만들기=============================================

#버튼 리스트
button_list = [(7, 1, 0), (8, 1, 1), (9, 1, 2), (4, 2, 0), (5, 2, 1), (6, 2, 2), (1, 3, 0), (2, 3, 1), (3, 3, 2), (".", 4, 0), (0, 4, 1),
               ("+", 4, 2), ("/", 1, 3), ("÷", 2, 3), ("x", 3, 3)]
for i, row, column in button_list:
    btn = tk.Button(root, text=i, command=lambda t=i: btn_click(t), width=10, height=5)
    btn.grid(row=row, column=column)

#람다 함수 쓴 이유:
#() 있어서 바로 호출되어야하지만 lambda 를 씀으로써 호출을 미룬 것

#=버튼
result_btn = tk.Button(root, text="=", width=10, height=5, command=calculate_result)
result_btn.grid(row=4, column=3)

#clear 전체 삭제 버튼
clear_btn = tk.Button(root, text="clear", command=clear_all, width=20, height=5)
clear_btn.grid(row=5, column=1, columnspan=2)

#del 하나씩 삭제 버튼
del_btn = tk.Button(root, text="DEL", command=del, width=10, height=5)
del_btn.grid(row= 5, column=3)



root.mainloop()


#0.2+2.1 = 2.30000003 -> 이진법 문제
#메모리 안에 저장할 때의 문제

#예외처리
#45+  처럼 수식이 안 끝났을 때 에러 띄우기
#연산자 연속으로 입력했을 떄 에러

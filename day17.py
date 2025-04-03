import tkinter as tk
from tkinter import messagebox

from PIL.ImageMath import lambda_eval


##기본 창 구성
root = tk.Tk()  #창 생성
root.title("GUI 프로그래밍 실습")  #창 제목(타이틀)
root.geometry("800x500") #창 크기 설정(가로x세로)
root.resizable(False, False)  #창 크기 조절 가능/불가능(가로, 세로)

##레이블 설정
label = tk.Label(root, text="안녕하세요", fg="red", bg="blue")
label.pack(side="top") #pack 을 해줘야함


##버튼만들기
def button_click():
    print("클릭됨")
    print(chk_var.get()) #35번 라인 코드의 체크된 상태를 보여주는 것
    print(radio_var.get())
    root.quit()   #프로그램을 종료

button = tk.Button(root, text="종료", command=button_click)  #command 버튼 클릭 시 실행될 것
button.pack(side="bottom")  #side="left"하면 레이블 다음으로 빈 공간없이 붙음

##entry 만들기 - 한 줄 입력창
entry = tk.Entry(root)
entry.pack(side="top")

##text 만들기 - 여러 줄 입력
text = tk.Text(root, wrap="char") # wrap => 줄바꿈 타입
#word : 단어 단위
#none : 줄 내림 하지 않음
#char : 글자 단위 줄바꿈
#word : 단어 단위로 줄바꿈
text.pack(side="top")

##check박스 만들기
chk_var = tk.IntVar()  #체크하면 0, 안하면 1  ->  체크된 상태를 나타냄
chk = tk.Checkbutton(root, text="위 내용에 거짓이 없음을 동의합니다.", variable=chk_var)
chk.pack(side="bottom")

def value_print():
    print(radio_var.get())

##Radiobutton 만들기
radio_var = tk.StringVar() #선택 옵션의 한 묶음  ->  value 에 문자열 넣었으므로 StringVar
r1 = tk.Radiobutton(root, text="옵션1", variable=radio_var, value="옵션1", command=value_print)  #text:글
r2 = tk.Radiobutton(root, text="옵션2", variable=radio_var, value="옵션2", command=value_print)  #value:골랐을 때 어떤 걸 받을지
r3 = tk.Radiobutton(root, text="옵션3", variable=radio_var, value="옵션3", command=value_print)
r1.pack(side="top")
r2.pack(side="top")
r3.pack(side="top")

root.mainloop()   #최종 실행 -> 가장 마지막에 있어야함



#===================================================================================
# #레이아웃
#
# root= tk.Tk()
# root.title("레이아웃 실습")
# root.geometry("800x600")
#
# label1 = tk.Label(root, text="안녕하세요")
# label1.place(x=0, y=0)
#
# label2 = tk.Label(root, text="반갑습니다")
# label2.place(x=30, y=800)  #column/row span: column/row 을 2칸으로 늘리는 것
#
# label3 = tk.Label(root, text="소통해요")
# label3.place(x=0, y=200)
#
# label4 = tk.Label(root, text="파이썬")
# label4.place(x=0, y=300)
#
#
# root.mainloop()


root = tk.Tk()
root.title("회원가입창")
root.geometry("500x200")

##ID 입력창 만들기
id_label = tk.Label(root, text="아이디 :")
id_label.grid(row=0, column=0, padx=10)    #pad x/y : 라벨 좌우/위아래 여유간격을 일정 픽셀 둠

id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, pady=5)


def dupl_click():
    tk.messagebox.showinfo("중복확인", "중복확인 되었습니다")  #1번째 인수: 창 이름  #2번째 인수: 메세지 내용
    # tk.messagebox.showerror() : 에러 메시지 창 띄우기 (빨간색)
    # tk.messagebox.showwarning() : 경고 메시지 창 띄우기 (노란색)

##ID 중복확인 버튼
dupl_btn = tk.Button(root, text="중복확인", command=dupl_click)
dupl_btn.grid(row=0, column=2)

##비밀번호 입력창 만들기
password_label = tk.Label(root, text="비밀번호 :")
password_label.grid(row=1, column=0, padx=10)

password_entry = tk.Entry(root, show="*")  #입력할 때 * 로 나오게 설정
password_entry.grid(row=1, column=1, pady=5)

##체크박스 만들기
chk_var = tk.IntVar()
chk = tk.Checkbutton(root, text="약관 내용에 동의합니다.", variable=chk_var)
chk.grid(row=2, column=1)


##회원가입 버튼 눌렀을 때 실행되는 메소드 설정
def signup_click():
    if chk_var.get() == 0:
        chk_value = "동의안함"
    else:
        chk_value = "동의함"
    tk.messagebox.showinfo("회원가입 완료", f"아이디: {id_entry.get()}\n 약관동의:{chk_value}")


signup_btn = tk.Button(root, text="회원가입", command=signup_click)  #회원가입 버튼
signup_btn.grid(row=3, column=2)

"""
아이디, 비번 입력 안되었을 경우
아이디 중복확인 여부 
"""

# ###예외처리
# try: id_entry
#
# except NotImplementedError
#         print("값을 입력해주세요")
#
#

#id_entry.get(): 아이디 입력창에 입력한 값 가져옴
root.mainloop()


#========================================================================================

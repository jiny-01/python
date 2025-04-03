import tkinter as tk
from tkinter import messagebox
import json
import os

SAVE_FILE = "save.json"            #모두 대문자로 쓴 것 -> 상수변수(변할 일 없음)


###메소드(기능) 은 선언(command) 하기 전에만 정의하면 됨
##기능 구현
#1) 추가 기능
def add_todo():
    todo = to_do_entry.get()  #entry 에 입력된 값  #하나라서 범위설정 안함?
    if todo:                   #todo 에 값이 존재할 경우
        to_do_list_box.insert(tk.END, todo)  #insert(어디에, 무엇을?)
        to_do_entry.delete(0, tk.END)        #입력창에 쓴 걸 추가하고 나면 지우기
    else:                      #입력안한 경우
        messagebox.showwarning("경고", "할 일을 입력하세요!")

#2) 삭제 기능
def remove_todo():
    try:
        todo = to_do_list_box.curselection()      #선택한 항목이 튜플형태
        if not todo:                              #선택된 것이 없을 경우
            raise IndexError
        to_do_list_box.delete(todo[0])       #튜플이기 때문에 하나 0번째
    except IndexError:
        messagebox.showwarning("경고", "삭제할 할 일을 선택하세요!")

#3) 전체삭제 기능
def clear_todo():
    if to_do_list_box.size() == 0:        #리스트박스의 항목 갯수 => 0이면 아무것도 없음
        messagebox.showwarning("경고", "삭제할 할 일이 없습니다!")
    else:                                 #리스트박스에 있을 경우
        to_do_list_box.delete(0, tk.END)  #처음부터 끝까지 다 지우기


#4) 저장하기 기능
def save_todo():
    todo_list = to_do_list_box.get(0, tk.END)     #튜플 형태로 다 들고옴  범위설정?
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(todo_list, file, indent=4, ensure_ascii=False)
        messagebox.showinfo("저장 완료", "저장이 완료되었습니다!")
    except Exception as e:
        messagebox.showerror("오류", f"저장 중 오류 발생: {e}")


#5) 불러오기 기능
def load_todo():
    if os.path.exists(SAVE_FILE):    #이 코드와 같은 경로에 SAVE_FILE 이 있으면
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as file:
                todo_list = json.load(file)
                if not isinstance(todo_list, list):    #todo_list 가 list 형태냐?
                    raise ValueError("올바른 형식이 아닙니다.")
                if to_do_list_box.size() != 0:       #목록에 다른 내용이 있을 경우
                    clear_todo()                     #전체 지우고 불러오기
                for todo in todo_list:
                    to_do_list_box.insert(tk.END, todo)   #insert(어디에, 무엇을?)
        except (json.JSONDecodeError, ValueError):   #json.JSONDecodeError: 제이슨 파일 불러올 때 뜰 수 있는 에러
            messagebox.showerror("오류", "파일 데이터가 손상되었습니다")
        except Exception as e:
            messagebox.showerror("오류", f"불러오기 중 오류 발생: {e}")
    else:
        messagebox.showwarning("경고", "불러올 저장 파일이 없습니다.")

#isinstance(a, list)  a가 list(광범위)형태냐
#type.list  => 좀 더 타이트한 범위


#==============================레이아웃 만들기================================================

##새 창 만들기
root = tk.Tk()
root.title("TO DO LIST")
root.geometry("400x500")

##Entry 만들기
to_do_entry = tk.Entry(root, width=40)
to_do_entry.pack(pady=10)

##Button 프레임 만들기
btn_frame = tk.Frame(root)
btn_frame.pack()

##Button 만들기
# 1) 추가버튼
add_btn = tk.Button(btn_frame, text="추가", width=10, command=add_todo)
add_btn.grid(row=0, column=0)
# 2) 삭제버튼
remove_btn = tk.Button(btn_frame, text="삭제", width=10, command=remove_todo)
remove_btn.grid(row=0, column=1, padx=20)
# 3) 전체삭제 버튼
clear_btn = tk.Button(btn_frame, text="전체삭제", width=10, command=clear_todo)
clear_btn.grid(row=0, column=2)

##목록 만들기
to_do_list_box = tk.Listbox(root, width=50, height=20)
to_do_list_box.pack(pady=10)

""""
selectmode의 종류
browse : 하나만 선택(클릭으로) -> 기본값(지정하지 않았을 경우)
single : 하나만 선택(스페이스바) - 방향키로 아래위 이동가능
extended : 여러 개 선택(쉬프트(연속)나 컨트롤키(낱개로 여러개)를 
           이용해 연속 또는 개별 선택)
multiple : 클릭할 때마다 선택/해제가 가능
"""

##아래쪽 버튼 만들기
btn_frame2 = tk.Frame(root)
btn_frame2.pack()

#1) 저장하기(save) 버튼
save_btn = tk.Button(btn_frame2, text="저장", command=save_todo)
save_btn.grid(row=0, column=0, padx=20)
#2) 불러오기(load) 버튼
load_btn = tk.Button(btn_frame2, text="불러오기", command=load_todo)
load_btn.grid(row=0, column=1, padx=20)

















root.mainloop() #창 실행
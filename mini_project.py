import tkinter as tk
from tkinter import messagebox
import json

root = tk.Tk()
root.title("환자리스트")
root.geometry("800x500")

#데이터 저장파일(불러올 파일)
patient_data = {}
DATA_FILE = "patient_data.json"

def save_data():
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as file:
                json.dump(patient_data, file, indent=4, ensure_ascii=False)
            messagebox.showinfo("저장 완료", "저장이 완료되었습니다!")
        except Exception as e:
            messagebox.showerror("오류", "저장 중 오류가 발생했습니다.")



def load_data():
    pass

def close():
    root.destroy()

#상단 프레임 설정
top_frame = tk.Frame(root)
top_frame.pack()

#"환자 정보"
label1 = tk.Label(root, text="환자정보", width=50, bg="lightgray", fg="black")
label1.grid(row=0, column=0, columnspan=2)

#이름, 성별, 나이, 병명,
name = tk.Label(top_frame, text="이름")
name.grid(row=1, column=0)
name_entry = tk.Entry(top_frame, width=20)
name_entry.grid(row=1, column=1)

#성별
gender = tk.Label(top_frame, text="성별")
gender.grid(row=1, column=2)

gender_var = tk.StringVar()
gender_var.set("남자")

male = tk.Radiobutton(top_frame, text="남자", variable=gender_var, value="남자")
female = tk.Radiobutton(top_frame, text="여자", variable=gender_var, value="여자")

male.grid(row=1, column=3)
female.grid(row=1, column=4, padx=30)


# 나이
age_label = tk.Label(top_frame, text="나이")
age_label.grid(row=2, column=0)
age_entry = tk.Entry(top_frame, width=30)
age_entry.grid(row=2, column=1)

# 병명
diagnosis_label = tk.Label(top_frame, text="병명")
diagnosis_label.grid(row=3, column=0)
diagnosis_entry = tk.Entry(top_frame, width=30)
diagnosis_entry.grid(row=3, column=1)




#환자 정보 입력
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=10)

#내용 입력
content = tk.Listbox(root, width=50)
content.pack(padx=10, pady=10)

#"시간별 기록"
label1 = tk.Label(root, text="시간별 기록", width=50, bg="lightgray", fg="black")
label1.pack(padx=10, pady=10)
#내용 입력
content2 = tk.Listbox(root, width=50)
content2.pack(padx=10, pady=10)

#하단 버튼 프레임-저장, 불러오기, 종료
button_frame = tk.Frame(root)
button_frame.pack(side="bottom")


#저장 버튼
save_btn = tk.Button(button_frame, text="저장", command=save_data)
save_btn.grid(row=0, column=0, padx=10)

#불러오기 버튼
load_btn = tk.Button(button_frame, text="불러오기", command=load_data)
load_btn.grid(row=0, column=1, padx=10)

#종료 버튼
close_btn = tk.Button(button_frame, text="종료", command=close)
close_btn.grid(row=0, column=2, padx=10)



root.mainloop()
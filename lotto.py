import tkinter as tk
import random

root = tk.Tk()
root.title("로또번호생성기")

#상단 프레임 설정
top_frame = tk.Frame(root)
top_frame.pack()

"""
랜덤 수 뽑기 - 6개 (중복없음, 0_ 형태도 표현), 오름차순
-표현식 바꾸기
-띄어쓰기로 join
-label
-번호 생성
"""


def create_numbers():
    count = int(set_spinbox.get())     #선택된 세트 횟수 가져오기 -> count로
    lines=[]   #한 세트에 생기는 6개의 숫자 세트
    for _ in range(count):
        number = sorted(random.sample(range(1, 46),6)) #random: 중복없이 랜덤 숫자 뽑기, sorted: 오름차순,
        formatted_nums = []
        for num in number:
            formatted_nums.append(f"{num:02d}")      #표현식 바꾸기- 한 자리일 때 0표기
        line = " ".join(formatted_nums)
        lines.append(line)

    text = "\n".join(lines)          #lines 에 한 줄에 6개 숫자 오게끔 줄바꿈 기준 조인
    result_label.config(text=text)   #라밸
    history.append(text)             #history 에 쌓이게끔


history = []

def show_history():
    screen = tk.Toplevel(root)            #히스토리 보여주는 새 창
    screen.title("기록")
    t = tk.Text(screen)                     #t = text를 의미
    for i, log in enumerate(history, 1):        #시작을 1부터 지정    enumerate(반복할 대상, 시작값): 요소뿐만 아니라 인덱스 값 같이 가져옴
        line = log.replace("\n", " | ")             #로그에 \n 인 부분 -> | 로 표기 대체
        t.insert(tk.END, f"{i}. {line}\n")
#i 는 1번쨰, 2번째,,,,, / log 는 한 번 생성할 때 뽑힌 숫자들 / i:line 는 줄바꿈으로 구분

    t.pack(fill="both", expand=True)

#=============================================버튼 만들기==============================================================

#생성 버튼
make_button = tk.Button(top_frame, text="생성", command=create_numbers)
make_button.grid(row=0, column=3, padx=5)


# 세트 수 라벨
set_label = tk.Label(top_frame, text="세트 수")
set_label.grid(row=0, column=1, padx=5)

# 세트 수 스핀박스 (0 ~ 10)
set_spinbox = tk.Spinbox(top_frame, from_=0, to=10, width=5)
set_spinbox.grid(row=0, column=2, padx=10)

# 숫자 보여줄 라벨
result_label = tk.Label(root, text="숫자", width=50, bg="lightgray", fg="black")
result_label.pack(pady=20)



#하단 버튼 프레임-저장, 불러오기, 종료
bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom")


#히스토리 버튼
history_btn = tk.Button(bottom_frame, text="히스토리", command=show_history)
history_btn.grid(row=0, column=0, padx=10)

#종료 버튼
close_btn = tk.Button(bottom_frame, text="종료", command=root.destroy)
close_btn.grid(row=0, column=1, padx=10)


#중복되지 않게 숫자 뽑는 - random.sample(인자1, 인자2)

root.mainloop()
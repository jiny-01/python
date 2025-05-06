import tkinter as tk
from tkinter import messagebox


#옵션 선택창, 결환 버튼, 기록 버튼, 결과 라벨 버튼
#결과 소수점 2번째 자리까지 나타내기


#새 창 만들기
root = tk.Tk()
root.title("변환기")

#내용 입력창
entry = tk.Entry(root, width = 50)
entry.grid(row=0, column=1)



#옵션 선택 시 리셋하는 메소드
def reset(select):
    entry.delete(0, tk.END)
    result_label.config(text="")
# 옵션메뉴에서 command 함수 지정할 땐 매개변수가 있어야함 -> reset(select)

log = []

#기록 가져오기
def load():
    log = tk.Toplevel(root)  # root 창 위에 Toplevel 창을 하나 더 만들기
    log.title("기록")


#옵션 선택 리스트
option = {
    "cm->inch":lambda x:x/2.54,
    "inch->cm":lambda x:x*2.54,
    "kg->lb":lambda x:x*2.20462,
    "lb->kg":lambda x:x/2.20462,
    "C->F":lambda x:x*9/5 + 32,
    "F->C":lambda x:(x-32)*5/9
}

# 키만 뽑아 리스트로 만들기
option_keys = list(option.keys())

var = tk.StringVar(root) #stringvar: 들어갈 수 있는 형태
var.set(option_keys[0])  #옵션 선택의 초기값 선택

# 옵션 메뉴 생성
optionmenu = tk.OptionMenu(root, var, *option_keys, command=reset)
#var: 기본값
#option_keys: 리스트로 만들었던 거 언패킹한 것
optionmenu.grid(row=1, column=1)



#변환하는 메소드-수식 적용
def convert():
    try:
        value = float(entry.get())  #entry 에 입력한 값- 소수점 있기 떄문에 float 변환 필요
        conv_type = var.get() #option 에서 선택된 값
        func = option[conv_type]  #옵션 딕셔너리에서 선택된 키의 값, 즉 람다 함수를 func 으로 가져옴
        result = func(value) #func 함수(람다 함수) 에 value 를 넣은 것 => result 로 받음
        result_label.config(text=f"결과: {result:0.2f}")
        for i in log:
            log.append(f"선택한 타입: {conv_type} 선택한 값: {func} => 결과: {result}")

    except ValueError:
        tk.messagebox.showerror("에러", "숫자를 입력하세요")
        result_label.config(text="숫자만 입력하세요")


#"변환"버튼
convert_btn = tk.Button(root, text="변환", command=convert, width=10, height=5)
convert_btn.grid(row=0, column=3, padx=50)

#기록 버튼
record_btn = tk.Button(root, text="기록보기", command=load, width=20, height=5)
record_btn.grid(row=5, column=9, columnspan=2)

#결과 보여주는 라벨창
result_label = tk.Label(root, text="결과:")
result_label.grid(row=1, column=0)





root.mainloop()





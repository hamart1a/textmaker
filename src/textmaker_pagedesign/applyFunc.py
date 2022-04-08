from tkinter import *
from tkinter import ttk


def make_apply_pop():
    win = Tk()
    win.title("적용버튼")
    win.geometry('200x100+200+200')
    textbox = ttk.Entry(win, width=20, textvariable=str)
    textbox.grid(column=0, row=0)

    apply_text = ""
    def apply(target_data_nm):
        apply_text = "-  '" + target_data_nm + "적용' 버튼을 클릭하면 적용가능한 " + target_data_nm + "목록을 조회하는 팝업창이 표시된다."
        win.destroy()

    action = ttk.Button(win, text="적용텍스트 생성", command=lambda: apply(textbox.get()))
    action.grid(column=0, row=1)
    win.mainloop()






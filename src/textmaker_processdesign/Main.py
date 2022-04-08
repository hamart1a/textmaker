from tkinter import *
from tkinter import ttk
import textFunc

window = Tk()

window.title("화면설계서 텍스트 생성기")
# window.geometry("640x400+100+100")
window.resizable(True, True)

# 등록 데이터명
label = Label(window, text="등록데이터").grid(row=3, column=0)
entry_target_data = Entry(window)
entry_target_data.grid(row=3, column=1)

# 텍스트
text_main = Text(window)
text_main.grid(row=4, column=0, columnspan=5)

# 체크박스
buttonText = [
    '저장', '조회', '신규', '수정', '삭제',
    '엑셀다운', '양식다운', '엑셀업로드', '적용','추가']

rowIndex = 1
colIndex = 0

for button_Text in buttonText:
    def insert_process(t=button_Text):
        target_data_nm = str(entry_target_data.get())
        insert_text = textFunc.make_process_text(t, target_data_nm)
        text_main.insert(END, insert_text)


    # 적용 팝업 생성
    def apply_process():
        win = Tk()
        win.title("적용버튼")
        win.geometry('200x100+200+200')
        textbox = ttk.Entry(win, width=20, textvariable=str)
        textbox.grid(column=0, row=0)

        def apply(target_data_nm):
            apply_text = "- '" + target_data_nm + "적용' 버튼을 클릭하면 적용가능한 " + target_data_nm + "목록을 조회하는 팝업창이 표시된다.\n"
            text_main.insert(END, apply_text)
            win.destroy()

        action = ttk.Button(win, text="적용텍스트 생성", command=lambda: apply(textbox.get()))
        action.grid(column=0, row=1)
        win.mainloop()


    if button_Text == '적용':
        Button(window, text=button_Text, width=10, command=apply_process).grid(row=rowIndex, column=colIndex)
    else:
        Button(window, text=button_Text, width=10, command=insert_process).grid(row=rowIndex, column=colIndex)

    colIndex += 1
    if colIndex > 4:
        rowIndex += 1
        colIndex = 0

# 만들기버튼
b_make = Button(window, text='프로세스설명생성').grid(row=5, column=0)


# 지우기버튼
def clear_text():
    text_main.delete(1.0, END)


b_clear = Button(window, text='지우기', command=clear_text).grid(row=5, column=1)


# 주요 항목 설명 복사 버튼

def copy_process():
    clip2 = Tk()
    clip2.withdraw()
    clip2.clipboard_clear()
    clip2.clipboard_append("⦁프로세스 설명\n")
    clip2.clipboard_append(text_main.get(1.0, END))
    clip2.destroy()


b_copy_process = Button(window, text='주요항목설명복사', command=copy_process).grid(row=5, column=2)


# 체크 사항 복사 버튼

def copy_notice():
    data = """⦁요구사항 및 제약사항
 - 필수입력항목 미 입력 시 경고 팝업 출력 및 저장제한"""
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(data)
    clip.destroy()


b_clear2 = Button(window, text='체크항목복사', command=copy_notice).grid(row=5, column=3)

window.mainloop()

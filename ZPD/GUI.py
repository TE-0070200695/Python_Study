import tkinter as Tk
import tkinter.font as ft
from tkinter.constants import END

def print_text():
    text = Tk.Label(frame_2,text=entry_1.get())
    text.pack()
    print("出力が押されました")
    entry_1.delete(0,END)

def count(number):
    value = number + 1
    text = Tk.Label(frame_2,text=number,bg='#499499')
    text.pack()

#ウィンドウの作成
root = Tk.Tk()
root.title('DACQ_GraphCreater')
root.geometry('500x600')
root.resizable(0,0)

#frameの作成
frame_1 = Tk.Frame(root,bg='yellow')
frame_2 = Tk.Frame(root,bg='green')
frame_3 = Tk.LabelFrame(root,text='よろしくお願いいたします。',borderwidth=5)
frame_4 = Tk.Frame(root,bg="skyblue",width=500,height=200)

frame_1.pack(fill='both')
frame_2.pack(fill='both')
frame_3.pack(fill='both')
frame_4.pack(padx=10,pady=10)

#ラベルの作成
label_1 = Tk.Label(frame_1,text="これはテストです").pack()

label_2 = Tk.Label(frame_2,text="これはテストです",font=('Arial',10,'bold'))
label_2.pack()

label_3 = Tk.Label(frame_3,text="これはテストです",font=('Arial',10,'bold'),bg='gray')
label_3.pack(padx=10,pady=10)

label_4 = Tk.Label(frame_1,text="これはテストです",font=('Arial',10,'bold'),bg='gray',fg='green')
label_4.pack(padx=10,pady=(0,10),ipadx=50,ipady=20,anchor='w')

label_5 = Tk.Label(frame_1,text="これはテストです",font=('Arial',10,'bold'),bg='gray',fg='green')
label_5.pack(padx=10,pady=(0,10),fill='both',expand=True)

#root.config(bg='red')
#フォントの確認
#print(ft.families())

#サブウィンドウの作成
sub_window = Tk.Toplevel()
sub_window.title('Graph_Preview')
sub_window.config(bg="#AA0000")
sub_window.geometry('300x600+500+30')

#ボタンの作成
button_1 = Tk.Button(frame_4,text='出力',command=print_text)
button_1.grid(row=0,column=1,padx=5,pady=5,ipadx=30)

button_2 = Tk.Button(sub_window,text='ボタン２')
button_2.grid(row=1,column=1)

button_3 = Tk.Button(sub_window,text='ボタン3',bg='pink',activebackground='yellow',borderwidth=5)
button_3.grid(row=1,column=0,padx=10,pady=10,ipadx=10,ipady=10)

#エントリーの作成
entry_1 = Tk.Entry(frame_4,width=30)
entry_1.grid(row=0,column=0,padx=10,pady=10)
frame_4.grid_propagate(0)

#引数を渡して関数を実行
value = 0
button_4 = Tk.Button(frame_4,text='カウント',command=lambda:count(value))
button_4.grid(row=1,column=1,columnspan=2,padx=5,pady=5)

#ウィンドウのループ処理
root.mainloop()
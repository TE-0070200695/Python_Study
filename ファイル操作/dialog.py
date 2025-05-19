import tkinter as tk
import tkinter.messagebox as mb

def tell_fortune():
    mb.showinfo("タイトル","本文です")

root = tk.Tk()
root.title("Python占い")
root.geometry("600x400")

    
desc_label = tk.Label(text="あなたの運勢を占います。下のボタンをクリックしてください。")#ラベルの作成
desc_label.pack()

ft_button = tk.Button(
    text = "占う",
    width = 100,
    height = 40,
    command = tell_fortune#ボタンのクリック時に呼ばれる関数を指定
)
ft_button.pack()

root.mainloop()
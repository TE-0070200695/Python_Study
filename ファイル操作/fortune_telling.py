import tkinter as tk
import tkinter.messagebox as mb

import random#乱数用のモジュール

result = [
    ["大吉","史上まれにみる幸運！"],
    ["吉","なかなかの幸運!"],
    ["中吉","まあ、幸運"],
    ["凶","幸運。。。かな？"],
    ["大凶","サンプルコード名ので気にしないでね。"]
]

def tell_fortune():
    rand = random.randrange(len(result))#0から(リストの長さ-1)までの範囲の乱数を整数で取得
    r = result[rand]#結果を取得
    mb.showinfo(r[0],r[1])#結果を表示

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
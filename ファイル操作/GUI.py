import tkinter as tk

root = tk.Tk()
root.title("Python占い")
root.geometry("600x400")

desc_label = tk.Label(text="あなたの運勢を占います。下のボタンをクリックしてください。")#ラベルの作成
desc_label.pack()

def tell_fortune():
    print("Fortune telling!")#この占いのロジックを描きます

ft_button = tk.Button(
    text = "占う",
    width = 100,
    height = 40,
    command = tell_fortune#ボタンのクリック時に呼ばれる関数を指定
)
ft_button.pack()

root.mainloop()
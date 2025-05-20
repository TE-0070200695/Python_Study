import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import filedialog

# ドロップされたファイルのリストを保持する変数
dropped_files = []

def drop_file(event):
    """ドラッグ＆ドロップされたファイルをリストに追加して表示"""
    global dropped_files
    # ドロップされたファイルのパスを取得し、リストに追加
    file_paths = event.data.strip().split()  # 複数ファイルの場合はスペース区切り
    dropped_files.extend(file_paths)

    # リストを更新して表示
    dropped_file_label.config(text="選択されたファイル:\n" + "\n".join(dropped_files))

def select_file():
    """ファイルを選択"""
    global dropped_files
    file_paths = filedialog.askopenfilename()
    dropped_files.extend(file_paths.strip().split())
    if dropped_files:
        # リストを更新して表示
        dropped_file_label.config(text="選択されたファイル:\n" + "\n".join(dropped_files))

def select_save_directory():
    """保存先ディレクトリを選択"""
    global directory
    directory = filedialog.askdirectory()
    if directory:
        save_directory_label.config(text=f"保存先ディレクトリ:{directory}")

def reset_files():
    """ファイルリストをリセット"""
    global dropped_files
    dropped_files = []  # リストを空にする
    dropped_file_label.config(text="選択されたファイル:\nなし")  # 表示を初期化

def reset_directory():
    """保存先ディレクトリをリセット"""
    global directory
    directory = ""
    save_directory_label.config(text=f"保存先ディレクトリ：なし")#表示を初期化

# TkinterDnD2を使用してウィンドウを作成
root = TkinterDnD.Tk()

# ウィンドウの設定
root.title("DACQ Graph Creator")  # ウィンドウタイトル
root.geometry("500x600")          # ウィンドウサイズ

# フレーム1: ファイルのドラッグ＆ドロップ
frame1 = tk.Frame(root, bg="lightblue", width=400, height=250)
frame1.pack_propagate(False)  # サイズ固定
frame1.pack(fill=tk.X)

frame1_label = tk.Label(frame1, text="ここにファイルをドラッグ＆ドロップしてください", bg="lightblue")
frame1_label.pack(pady=20)

dropped_file_label = tk.Label(frame1, text="選択されたファイル:なし", bg="lightblue", justify="left")
dropped_file_label.pack(pady=10)

select_button2 = tk.Button(frame1, text="ファイルを選択", command=select_file)
select_button2.pack(pady=10)

# リセットボタンを追加
reset_button = tk.Button(frame1, text="リセット", command=reset_files)
reset_button.pack(pady=10)

# ドロップイベントをバインド
frame1.drop_target_register(DND_FILES)
frame1.dnd_bind('<<Drop>>', drop_file)

# フレーム2: 保存先ディレクトリの指定
frame2 = tk.Frame(root, bg="lightgreen", width=400, height=150)
frame2.pack_propagate(False)  # サイズ固定
frame2.pack(fill=tk.X)

frame2_label = tk.Label(frame2, text="保存先ディレクトリを選択してください", bg="lightgreen")
frame2_label.pack(padx=20)

save_directory_label = tk.Label(frame2, text="保存先ディレクトリ:なし", bg="lightgreen", justify="left")
save_directory_label.pack(pady=10)

select_button = tk.Button(frame2, text="保存先を選択", command=select_save_directory)
select_button.pack(padx=20)

#リセットボタンを追加
reset_button2 = tk.Button(frame2,text="リセット",command=reset_directory)
reset_button2.pack(pady=10,padx=20)

# メインループを開始
root.mainloop()
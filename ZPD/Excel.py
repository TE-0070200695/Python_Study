import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt

class ExcelGraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Graph App")

        # ファイル名ラベルとエントリー
        self.label = tk.Label(root, text="ファイル名")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.file_entry = tk.Entry(root, width=40)
        self.file_entry.grid(row=0, column=1, padx=10, pady=10)

        # ファイル選択ボタン
        self.select_button = tk.Button(root, text="選択", command=self.select_file)
        self.select_button.grid(row=0, column=2, padx=10, pady=10)

        # グラフ作成ボタン
        self.plot_button = tk.Button(root, text="グラフ作成", command=self.plot_graph)
        self.plot_button.grid(row=1, column=1, padx=10, pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xlsm")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)

    def plot_graph(self):
        file_path = self.file_entry.get()
        
        if file_path:
            try:
                # Excelファイルを読み込む
                df = pd.read_excel(file_path, sheet_name='軸上_F4')  # シート名を適宜変更
                Get_df = df.iloc[11,]
                Get_df
            except Exception as e:
                messagebox.showerror("Error", f"エラーが発生しました: {e}")
        else:
            messagebox.showerror("Error", "ファイルを選択してください")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelGraphApp(root)
    root.mainloop()
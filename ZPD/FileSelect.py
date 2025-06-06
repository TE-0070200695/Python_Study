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
                df = pd.read_excel(file_path, sheet_name='Data',usecols='C,M,L')  # シート名を適宜変更
                
                # 特定のセルの文字列が同じ列だけをフィルタリング
                target_string = "2ton100%"  # ここにフィルタリングする文字列を指定
                filtered_df = df[df.iloc[12, 'C'] == target_string]  # 例として1列目をフィルタリング

                x_data =df[df['列2']=='2ton100%']
                y_data = df[df['列2']=='2ton100%']

                # 散布図をプロット
                plt.figure(figsize=(10, 6))
                plt.scatter(x_data, y_data)
                plt.title('Scatter Plot')
                plt.xlabel('X軸')
                plt.ylabel('Y軸')
                plt.grid(True)
                plt.show()
            except Exception as e:
                messagebox.showerror("Error", f"エラーが発生しました: {e}")
        else:
            messagebox.showerror("Error", "ファイルを選択してください")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelGraphApp(root)
    root.mainloop()
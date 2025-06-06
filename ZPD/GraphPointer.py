import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib import rcParams

# フォント設定を変更（日本語フォントを指定）
rcParams['font.sans-serif'] = ['MS Gothic']  # MS Gothicを使用

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("関数グラフ描画ツール")

        # ウィンドウを常に前面に表示
        self.root.attributes("-topmost", True)

        self.create_widgets()
        self.plot_graph()

        # ウィンドウのバツボタンが押されたときにプログラムを終了する設定
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # マウスホイールで拡大縮小
        self.root.bind("<MouseWheel>", self.on_mouse_wheel)

        # マウスドラッグでグラフ移動
        self.canvas.mpl_connect("button_press_event", self.on_mouse_press)
        self.canvas.mpl_connect("button_release_event", self.on_mouse_release)
        self.canvas.mpl_connect("motion_notify_event", self.on_mouse_move)

        # 拡大縮小倍率
        self.zoom_factor = 1.1

        # マウスドラッグ用変数
        self.dragging = False
        self.prev_mouse_x = None
        self.prev_mouse_y = None

        # 曲線データ保存用
        self.curves = []

    def create_widgets(self):
        # 関数1の入力
        ttk.Label(self.root, text="関数1").grid(row=0, column=0, padx=5, pady=5)
        self.entry_func1 = ttk.Entry(self.root)
        self.entry_func1.insert(0, "x")
        self.entry_func1.grid(row=0, column=1, padx=5, pady=5)
        self.entry_func1.bind("<KeyRelease>", self.on_key_release)

        ttk.Label(self.root, text="傾き").grid(row=0, column=2, padx=5, pady=5)
        self.entry_a1 = ttk.Entry(self.root)
        self.entry_a1.insert(0, "1")
        self.entry_a1.grid(row=0, column=3, padx=5, pady=5)
        self.entry_a1.bind("<KeyRelease>", self.on_key_release)

        # 関数2の入力
        ttk.Label(self.root, text="関数2").grid(row=1, column=0, padx=5, pady=5)
        self.entry_func2 = ttk.Entry(self.root)
        self.entry_func2.insert(0, "x")
        self.entry_func2.grid(row=1, column=1, padx=5, pady=5)
        self.entry_func2.bind("<KeyRelease>", self.on_key_release)

        ttk.Label(self.root, text="傾き").grid(row=1, column=2, padx=5, pady=5)
        self.entry_a2 = ttk.Entry(self.root)
        self.entry_a2.insert(0, "1")
        self.entry_a2.grid(row=1, column=3, padx=5, pady=5)
        self.entry_a2.bind("<KeyRelease>", self.on_key_release)

        # x軸の範囲入力
        ttk.Label(self.root, text="X軸").grid(row=2, column=0, padx=5, pady=5)
        self.entry_x_min = ttk.Entry(self.root)
        self.entry_x_min.insert(0, "-10")
        self.entry_x_min.grid(row=2, column=1, padx=5, pady=5)
        self.entry_x_min.bind("<KeyRelease>", self.on_key_release)

        ttk.Label(self.root, text="～").grid(row=2, column=2, padx=5, pady=5)
        self.entry_x_max = ttk.Entry(self.root)
        self.entry_x_max.insert(0, "10")
        self.entry_x_max.grid(row=2, column=3, padx=5, pady=5)
        self.entry_x_max.bind("<KeyRelease>", self.on_key_release)

        ttk.Label(self.root, text="間隔").grid(row=2, column=4, padx=5, pady=5)
        self.entry_x_interval = ttk.Entry(self.root)
        self.entry_x_interval.insert(0, "1")
        self.entry_x_interval.grid(row=2, column=5, padx=5, pady=5)
        self.entry_x_interval.bind("<KeyRelease>", self.on_key_release)

        # y軸の範囲入力
        ttk.Label(self.root, text="Y軸").grid(row=3, column=0, padx=5, pady=5)
        self.entry_y_min = ttk.Entry(self.root)
        self.entry_y_min.insert(0, "-10")
        self.entry_y_min.grid(row=3, column=1, padx=5, pady=5)
        self.entry_y_min.bind("<KeyRelease>", self.on_key_release)

        ttk.Label(self.root, text="～").grid(row=3, column=2, padx=5, pady=5)
        self.entry_y_max = ttk.Entry(self.root)
        self.entry_y_max.insert(0, "10")
        self.entry_y_max.grid(row=3, column=3, padx=5, pady=5)
        self.entry_y_max.bind("<KeyRelease>", self.on_key_release)

        ttk.Label(self.root, text="間隔").grid(row=3, column=4, padx=5, pady=5)
        self.entry_y_interval = ttk.Entry(self.root)
        self.entry_y_interval.insert(0, "1")
        self.entry_y_interval.grid(row=3, column=5, padx=5, pady=5)
        self.entry_y_interval.bind("<KeyRelease>", self.on_key_release)

        # 軸初期化ボタン
        self.reset_button = ttk.Button(self.root, text="軸初期化", command=self.reset_axes)
        self.reset_button.grid(row=4, column=0, columnspan=6, padx=5, pady=10)

        # グラフ描画用キャンバス
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().grid(row=5, column=0, columnspan=6, padx=5, pady=5)

        # 座標表示用ラベル
        self.coord_label = ttk.Label(self.root, text="Coordinates: ")
        self.coord_label.grid(row=6, column=0, columnspan=6, padx=5, pady=5)

    def reset_axes(self):
        # 初期値を設定
        self.entry_func1.delete(0, tk.END)
        self.entry_func1.insert(0, "x")
        self.entry_a1.delete(0, tk.END)
        self.entry_a1.insert(0, "1")

        self.entry_func2.delete(0, tk.END)
        self.entry_func2.insert(0, "x")
        self.entry_a2.delete(0, tk.END)
        self.entry_a2.insert(0, "1")

        self.entry_x_min.delete(0, tk.END)
        self.entry_x_min.insert(0, "-10")
        self.entry_x_max.delete(0, tk.END)
        self.entry_x_max.insert(0, "10")
        self.entry_x_interval.delete(0, tk.END)
        self.entry_x_interval.insert(0, "1")

        self.entry_y_min.delete(0, tk.END)
        self.entry_y_min.insert(0, "-10")
        self.entry_y_max.delete(0, tk.END)
        self.entry_y_max.insert(0, "10")
        self.entry_y_interval.delete(0, tk.END)
        self.entry_y_interval.insert(0, "1")

        # グラフを再描画
        self.plot_graph()

    def on_key_release(self, event):
        self.plot_graph()

    def plot_graph(self):
        try:
            func1 = self.entry_func1.get()
            a1 = float(self.entry_a1.get())
        except ValueError:
            func1 = "x"
            a1 = 1

        try:
            func2 = self.entry_func2.get()
            a2 = float(self.entry_a2.get())
        except ValueError:
            func2 = "x"
            a2 = 1

        try:
            x_min = float(self.entry_x_min.get())
        except ValueError:
            x_min = -10

        try:
            x_max = float(self.entry_x_max.get())
        except ValueError:
            x_max = 10

        try:
            y_min = float(self.entry_y_min.get())
        except ValueError:
            y_min = -10

        try:
            y_max = float(self.entry_y_max.get())
        except ValueError:
            y_max = 10

        try:
            x_interval = float(self.entry_x_interval.get())
        except ValueError:
            x_interval = 1

        try:
            y_interval = float(self.entry_y_interval.get())
        except ValueError:
            y_interval = 1

        x = np.linspace(x_min, x_max, 400)
        y1 = a1 * eval(func1)
        y2 = a2 * eval(func2)

        self.ax.clear()
        self.ax.plot(x, y1, label=f"y = {a1} * {func1}")
        self.ax.plot(x, y2, label=f"y = {a2} * {func2}")
        self.ax.legend()
        self.ax.set_title("2つの関数のグラフ")
        self.ax.set_xlim(x_min, x_max)
        self.ax.set_ylim(y_min, y_max)
        self.ax.set_xticks(np.arange(x_min, x_max + x_interval, x_interval))
        self.ax.set_yticks(np.arange(y_min, y_max + y_interval, y_interval))
        self.ax.grid(True)  # グリッドを表示
        self.canvas.draw()

        # 曲線データを保存
        self.curves = [(x, y1), (x, y2)]

    def on_mouse_wheel(self, event):
        # マウスホイールで拡大縮小
        if event.delta > 0:  # ホイールを奥に回すと拡大
            self.zoom_factor = 1.1
        else:  # ホイールを手前に回すと縮小
            self.zoom_factor = 0.9

        # x軸とy軸の範囲を拡大縮小
        x_min = float(self.entry_x_min.get())
        x_max = float(self.entry_x_max.get())
        y_min = float(self.entry_y_min.get())
        y_max = float(self.entry_y_max.get())

        x_min = round(x_min / self.zoom_factor, 2)
        x_max = round(x_max / self.zoom_factor, 2)
        y_min = round(y_min / self.zoom_factor, 2)
        y_max = round(y_max / self.zoom_factor, 2)

        self.entry_x_min.delete(0, tk.END)
        self.entry_x_min.insert(0, str(x_min))
        self.entry_x_max.delete(0, tk.END)
        self.entry_x_max.insert(0, str(x_max))
        self.entry_y_min.delete(0, tk.END)
        self.entry_y_min.insert(0, str(y_min))
        self.entry_y_max.delete(0, tk.END)
        self.entry_y_max.insert(0, str(y_max))

        self.plot_graph()

    def on_mouse_press(self, event):
        self.dragging = True
        self.prev_mouse_x = event.x
        self.prev_mouse_y = event.y

    def on_mouse_release(self, event):
        self.dragging = False
        self.prev_mouse_x = None
        self.prev_mouse_y = None

    def on_mouse_move(self, event):
        if self.dragging:
            dx = event.x - self.prev_mouse_x
            dy = event.y - self.prev_mouse_y

            x_min, x_max = self.ax.get_xlim()
            y_min, y_max = self.ax.get_ylim()

            x_min = round(x_min - dx * 0.05, 2)
            x_max = round(x_max - dx * 0.05, 2)
            y_min = round(y_min + dy * 0.05, 2)
            y_max = round(y_max + dy * 0.05, 2)

            self.ax.set_xlim(x_min, x_max)
            self.ax.set_ylim(y_min, y_max)

            self.prev_mouse_x = event.x
            self.prev_mouse_y = event.y

            self.canvas.draw()
        else:
            if event.inaxes:
                mouse_x, mouse_y = event.xdata, event.ydata
                closest_coords = self.get_closest_coords(mouse_x, mouse_y)
                self.coord_label.config(text=f"Coordinates: {closest_coords}")

    def get_closest_coords(self, mouse_x, mouse_y):
        closest_x, closest_y = None, None
        min_distance = float('inf')

        for curve_x, curve_y in self.curves:
            distances = np.sqrt((curve_x - mouse_x)**2 + (curve_y - mouse_y)**2)
            closest_index = np.argmin(distances)
            if distances[closest_index] < min_distance:
                min_distance = distances[closest_index]
                closest_x, closest_y = curve_x[closest_index], curve_y[closest_index]

        return f"({closest_x:.2f}, {closest_y:.2f})"

    def on_closing(self):
        # キャンバスのリソースを解放
        if self.canvas is not None:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None

        # Tkinterウィンドウを閉じる
        self.root.quit()  # イベントループを終了
        self.root.destroy()  # ウィンドウを破棄

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
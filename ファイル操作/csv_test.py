import csv #csvモジュールをインポート

stock = [["pen",24],["Apple",14],["Pineapple",8]]#二重のリスト

with open("stock.csv","w",encoding="Shift_jis") as f:#文字コードをShift_JISに指定
    writer = csv.writer(f,lineterminator="\n") #writeオブジェクトの作成　改行記号で行を区切る
    writer.writerows(stock)#csvファイルに書き込み

with open("stock.csv","r",encoding="Shift_jis")as f:
    reader = csv.reader(f)#readerオブジェクトの作成

    for r in reader:#for分を用いて一行ずつ読み込む
        print(f)
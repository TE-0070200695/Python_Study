try:
    with open("pico.txt") as f:
        print(f.read())
except FileNotFoundError as e:#FileNotFoundErrorは例外クラス名
    print("ファイルが見つかりません")
except Exception as e:
    print(e)

fruits = ["Apple","pineapple","orange"]

try:
    print(fruits[3])#範囲外の要素にアクセス
except IndexError as e: #IndexErroは範囲外の要素にアクセスした例文
    print("インデックスが範囲外です")

except Exception as e:
    print(e)
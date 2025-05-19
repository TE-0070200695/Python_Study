f = open("greetings.txt","r")#ファイルを開く "r"を指定すると読み込み
a = f.read() #ファイルの中身をすべて読み込む
f.close() #ファイルを閉じる

print(a)

f = open("greetings.txt","r")
for g in f:#各行を読み込んでaに入れる
    print(a.strip()) #strip()で改行を削除
f.close()

f = open("greetings.txt","r")
a = list(f)#ファイルの中身をリストに読み込む
f.close()

print(a) #リストを表示
for b in a:
    print(b.strip())

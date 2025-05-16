greetings = "Good morning!\nGood afternoon!\nGood evening!\nGood night!" #\nは改行記号

f = open("greetings.txt","w") #ファイルを開く "w"を指定すると書き込み
a = f.write(greetings)#ファイルに書き込んで、書き込んだ文字数を得る
f.close()#ファイルを閉じる

print(a)

#write("ファイル名","書き込みか読み込みか")  戻り値：文字数

f = open("greetings.txt","w")
for g in greetings:
    f.write(greetings)#リストの各要素をファイルに書き込み
f.close()
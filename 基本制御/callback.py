def showResult(a,b,callback):
    c = callback(a,b)
    print(c)

#関数後半に引数と動作を定義できる
showResult(3,4,lambda a,b:a + b)
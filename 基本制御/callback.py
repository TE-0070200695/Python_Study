def showResult(a,b,callback):
    c = callback(a,b)
    print(c)

showResult(3,4,lambda a,b:a +b)
def getNumber():
    a = 123
    return a
b = getNumber()
print(b)

def addAndMultiply(a,b):
    c = a+b
    d = a*b
    return (c,d)
result = addAndMultiply(3,4)
print(result)

#無名関数というものがある
GetNum = getNumber
print(GetNum())

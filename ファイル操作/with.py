fruits = "Apple\nPineapple\nOrange\nStrawberry"

with open("fruits.txt","w") as f: #with構文 close()を呼ばなくてもよい
    f.write(fruits)

with open("fruits.txt","r") as f:
    print(f.read())

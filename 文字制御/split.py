#splitで区切る
a = "ペンpicoパイナップルpicoりんごpicoぺん"
b = a.split("pico")
print(b)

#joinで文字列の間に追加する
c = "Pico".join(b)
print(c)

d = a.replace("pico","  ")
print(d)

e = "          Pen Pineapple Apple Pen!  "
f = e.strip()
print(f)
#strip("#")のように特定の文字を削除することができる

print(len(a))
g = a[3:12]
print(g)

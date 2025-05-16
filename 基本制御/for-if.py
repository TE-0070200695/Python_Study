a = [1,4,5,8,9,13,14,15,16,20,21]
for b in a:
    if b%2 == 1:
        print(b)

b=0
while b < len(a):
    c = a[b]
    if c%2 == 1:
        print(c)
    b +=1

b=0
while b < len(a):
    c = a[b]
    if c%2 == 0:
        print(c)
    b +=1


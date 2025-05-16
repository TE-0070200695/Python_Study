a = [1,2,3,4,5,6,7]
b =[]

for i in range(0,len(a),1):
    b.append(a[i]*2)
    print(b)

print("\n")

d = [c*2 for c in a]
print(d)

e = [c*2 for c in a if c < 5]
print(e)
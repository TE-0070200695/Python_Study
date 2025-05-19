class Pico1:
    def __str__(self):
        return "I have a pen."

p1 = Pico1()
print(str(p1))

class Pico2:
    def __call__(self,p,a):
        return p*5 + a*3
p2 = Pico2()
print(p2("りんご","パイナップル")) #p2を関数のように扱える

test = "Hello!!"
print(test*2)
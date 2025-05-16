class Pico1:
    def setFruit(self):
        self.apple = "りんご"#インスタンス変数を設定
        self.pine = "パイナップル" #インスタンス変数を設定

p1 = Pico1()
p1.setFruit()

print(p1.apple)#インスタンス変数にアクセス
print(p1.pine)#インスタンス変数にアクセス

class Pico2:
    def setFruit(self):
        self.apple = "りんご"
        self.pine = "パイナップル"
p2 = Pico2()
p2.setFruit()
p2.apple="あっぷる"
print(p2.apple)#appleがインスタンス変数に設定されていない
print(p2.pine)

class Pico3:
    def setFruit(self,ap,pi): #引数としてapとpiを受け取る
        self.apple=ap #インスタンス変数を設定
        self.pine = pi
pj = Pico3()
pj.setFruit("りんご","パイナップル")#selfで渡さなくて良い

pe = Pico3()#pjとは異なるインスタンス
pe.setFruit("Apple","Pineapple")

print(pj.apple,pj.pine)
print(pe.apple,pe.pine)
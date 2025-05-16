#コンストラクタ(イニシャライザ)の実装
class Pico1():
    def __init__(self,ap,pi):#コンストラクタ
        self.apple=ap
        self.pine=pi

    def sayAP(self):
        print(self.apple,self.pine)
p1 = Pico1("りんご","パイナップル")#インスタンスの生成　引数としてインスタンス変数の値を渡す
p1.sayAP()

#コンストラクタ(イニシャライザ)の実装
class Pico2():
    def __init__(self,ap="りんご",pi="パイナップル"):#コンストラクタ
        self.apple=ap
        self.pine=pi

    def sayAP(self):
        print(self.apple,self.pine)
p2 = Pico2()#値を渡さないといけない
p2.sayAP()


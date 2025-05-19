class Pico:#クラス　設計図のようなもの
    def sayPPAP(self):#メソッド　関数に似ている
        print("PPAP!")

P = Pico() #クラスからインスタンスを生成、pがインスタンス
P.sayPPAP() #メソッドの呼び出し

class Greeting1:
    def sayHello(self):#メソッド
        print("hello!")


gr_1 = Greeting1() #インスタンスの生成
gr_1.sayHello() #メソッドの呼び出し 

print("\n")

class Greeting2:
    def sayHello(self):#メソッド
        print("hello!")
    
    def sayNice(self):
        self.sayHello() #selfはインスタンス自身　インスタンスから他のメソッドを呼び出す
        print("Nice to meet you!")

gr_2 = Greeting2()
gr_2.sayNice()
class Human:
    name="" 
    age = 0
    bron = ""

    def __init__(self,name,age,born):#コンストラクタ
        self.name=name
        self.age = age
        self.born = born

    def talk(self):
        print("私の名前は"+self.name + "です")

    def walk(self):
        print("歩く")

    def sleep(self):
        print("寝る")
        
taro = Human("太郎",20,"東京")
#taro = Human()#インスタンスの生成
#taro.name = "太郎"#インスタンス変数の定義
#taro.age=20
#taro.born = "東京"
taro.talk()#メソッドの呼び出し

hanako = Human("花子",30,"大阪")
#hanako = Human()
#hanako.name = "花子"
#hanako.age=30
#hanako.born = "大阪"
hanako.talk()

jiro = Human("二郎",18,"福岡")
jiro.talk()
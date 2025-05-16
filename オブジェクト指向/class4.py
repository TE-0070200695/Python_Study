class Pico1:
    apple = "Apple"#クラス変数を定義
    pine = "Pineapple"

p1 = Pico1()
print(p1.apple)#インスタンス変数にアクセス　エラーにならずにクラス変数の値を取得

class Pico2:
    apple = "Apple"
    pine = "Pineapple"

p2 = Pico2()
p2.apple = "りんご" #インスタンス変数の値を変更
print(p2.apple)

print(Pico2.apple)

class Pico3:
    fruits = "apples"
    number = 0
    
    def getFruits(self):
        return "I have " + str(self.number) + " " + self.fruits + "."

p3 = Pico3()
print(p3.getFruits())

p3.fruits = "pineapples"
p3.number = 3
print(p3.getFruits())
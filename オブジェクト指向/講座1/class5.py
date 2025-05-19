class Dog:
    color = "brown"

    def bark(self):
        print("bow-wow!")

dog = Dog()
print(dog.color)
dog.bark()

class Shibainu(Dog):#()内に継承元クラス
    name = "Pochi" #新たにクラス変数を追加

    def sayName(self):#新たにメソッドを追加
        print("I'm " + self.name + ".")

shiba = Shibainu()
print(shiba.color)#継承元の変数
shiba.bark()#継承元のメソッド

print(shiba.name)#新たな変数
shiba.sayName()#新たなメソッド
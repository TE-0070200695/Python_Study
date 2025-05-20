class Circle:
    pi = 3.14#円周率
    __pi = 3.14 #クラスの中からしかアクセスできない(private変数)
    def length(self,r):
        return r * 2 * Circle.pi
    
    def area(self,r):
        return r * r * Circle.pi
    
    def length2(self,r):
        return r * 2 * Circle.__pi
    
print(Circle.pi)#クラス変数の呼び出し
print(Circle().length2(1))

class Circle:
    pi = 3.14#円周率

    def length(self,r):
        return r * 2 * Circle.pi
    
    def area(self,r):
        return r * r * Circle.pi
    
print(Circle.pi)#クラス変数の呼び出し

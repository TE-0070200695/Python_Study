class order:
    tax = 1.1

    def __init__(self,price,count):
        self.price = price
        self.count = count

    def total_price(self):
        total = self.price*self.count*self.tax
        total = int(total)
        print("合計金額は"+str(total)+ "円です。")

Order = order(100,10)
Order.total_price()

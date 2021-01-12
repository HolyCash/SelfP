class Apple:
    def __init__(self,c,s,p):
        self.color = c
        self.size = s
        self.price = p
        print("Создано")
app1 = Apple("green","big", 10)
print(app1.size)
print(app1.price)

from animal import Animal

class Pet (Animal):
    category = '未知' # 种类
    def __init__(self):
        print(self.category + '是宠物')



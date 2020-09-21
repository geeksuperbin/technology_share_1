from pet import Pet

class Dog (Pet):

    def __init__(self):
        self.category = '狗'
        # 继承父类构造方法
        super(Dog, self).__init__()

    def call(self):
        print('汪汪~~')



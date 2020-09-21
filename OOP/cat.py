from pet import Pet

class Cat (Pet):

    def __init__(self):
        self.category = '猫'
        # 继承父类构造方法
        super(Cat, self).__init__()

    def call(self):
        print('喵喵~~')



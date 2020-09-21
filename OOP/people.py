from animal import Animal

class People (Animal):
    sex = '未知'
    def __init__(self, sex):
        self.sex = sex
        print('我是人类')


    def call(self):
        """
        重写方法
        """
        print('我会讲道理')


    def say_sex(self):
        print('性别：', self.sex)
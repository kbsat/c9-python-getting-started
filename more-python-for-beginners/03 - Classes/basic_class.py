class Presenter():
    def __init__(self, name):
        # 생성자
        self.name = name

    def say_hello(self):
        # 메소드
        print('Hello, ' + self.name)


presenter = Presenter('Chris')
presenter.name = 'Christopher'
presenter.say_hello()

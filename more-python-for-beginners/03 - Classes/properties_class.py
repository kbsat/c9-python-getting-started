class Presenter():
    def __init__(self, name):
        # 생성자
        self.name = name

    @property
    def name(self):
        print('Retrieving name...')
        return self.__name

    @name.setter
    def name(self, value):
        # 유효성 검사에 효과적입니다.
        print('Validating name...')
        self.__name = value


presenter = Presenter('Chris')
presenter.name = 'Christopher'
print(presenter.name)

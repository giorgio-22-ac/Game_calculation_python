
from random import randint


class Calculate:

    def __init__(self, difficulty, /):
        self.__difficulty = difficulty
        self.__value1 = self._get_value
        self.__value2 = self._get_value
        self.__operation = randint(1, 3)  # 1 = sum, 2 = remove, 3 = multiply
        self.__result = self._get_result

    @property
    def difficulty(self):
        return self.__difficulty

    @property
    def value1(self):
        return self.__value1

    @property
    def value2(self):
        return self.__value2

    @property
    def operation(self):
        return self.__operation

    @property
    def result(self):
        return self.__result

    def __str__(self):
        op: str = ''
        if self.operation == 1:
            op = 'Sum'
        elif self.operation == 2:
            op = 'Remove'
        elif self.operation == 3:
            op = 'Multiplication'
        else:
            op = 'Operation unknown'
        return f'Value 1 : {self.value1} \nValue 2: {self.value2} \
            \nDifficulty: {self.difficulty} \nOperation: {op}'

    @property
    def _get_value(self):
        if self.difficulty == 1:
            return randint(0, 10)
        elif self.difficulty == 2:
            return randint(0, 100)
        elif self.difficulty == 3:
            return randint(0, 1000)
        elif self.difficulty == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _get_result(self):
        if self.operation == 1:
            return self.value1 + self.value2
        elif self.operation == 2:
            return self.value1 - self.value2
        else:
            return self.value1 * self.value2

    @property
    def _op_symbol(self):
        if self.operation == 1:
            return '+'
        elif self.operation == 2:
            return '-'
        else:
            return '*'

    def _check_result(self, result):
        right = False
        if self.result == result:
            print('The answer is correct!')
            right = True
        else:
            print('The answer is not correct!')
        print(f'{self.value1} {self._op_symbol} {self.value2} = {self.result}')
        return right

    def _show_operation(self):
        print(f'{self.value1} {self._op_symbol} {self.value2} = ?')

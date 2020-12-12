

class Calculator(object):
    '''Class Calculator '''
    def __init__(self, initial_amount = None ):
        self.value = initial_amount

    def add_two_numbers(self, a, b):
        self.value = a + b

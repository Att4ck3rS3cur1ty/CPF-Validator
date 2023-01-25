'''Module to calculate the statistics'''
from messages_validation import *

class Statistics:
    '''Calculates the statistics regarding the CPFs filtration'''
    def __init__(self, valid_cpf = 0, invalid_cpf = 0):
        self._valid_cpf = valid_cpf
        self._invalid_cpf = invalid_cpf

    def get_amount_valid_cpf(self):
        '''Get method to return the amount of valid CPFs'''
        return self._valid_cpf

    def set_amount_valid_cpf(self, valid_cpf_counter):
        '''Set method to store the amount of valid CPFs'''
        self._valid_cpf = valid_cpf_counter

    def get_amount_invalid_cpf(self):
        '''Get method to return the amount of invalid CPFs'''
        return self._invalid_cpf

    def set_amount_invalid_cpf(self, invalid_cpf_counter):
        '''Set method to store the amount of invalid CPFs'''
        self._invalid_cpf = invalid_cpf_counter

    def average_filtered_cpf(self):
        '''Calculates the average of valid CPFs versus invalid CPFs amount'''
        average = 0
        print(Messages.AMOUNT_VALID + str(self.get_amount_valid_cpf()))
        print(Messages.AMOUNT_INVALID + str(self.get_amount_invalid_cpf()))

        if self.get_amount_invalid_cpf() == 0:
            print(Messages.AVERAGE + "100 %")
        else:
            average = self.get_amount_valid_cpf() / self.get_amount_invalid_cpf()
            print(Messages.AVERAGE + str(f'{average:.2f}') + "%" + "\n")

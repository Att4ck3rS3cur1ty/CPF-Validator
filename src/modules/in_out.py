'''Module to handle the input and output files'''
import sys
from messages_validation import Messages

class IOchecker:
    messages_validation = Messages()
    '''Responsible for the IO logic'''
    def __init__(self, path):
        '''initiates the variables'''
        self.path = path
        self.first_write = True
        self.mode = "w"

    def input_file(self, path):
        '''reads the input CPF list file'''
        try:
            i_file = open(path, mode="r", encoding="utf-8")
            return i_file
        except Exception as exception:
            print(Messages.FAILED_OPEN_FILE + str(exception))
            return sys.exit(1)

    def output_file(self, path, content):
        '''writes valid CPF's to an external file'''
        try:
            if not self.first_write:
                self.mode = "a"
            o_file = open(path, mode=self.mode, encoding="utf-8")
            o_file.write(content)
            self.first_write = False
            return o_file
        except Exception as exception:
            print(Messages.FAILED_OPEN_FILE + str(exception))
            return sys.exit(1)

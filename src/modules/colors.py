'''Module to configure the script colors'''
class ByteColors:
    '''Used to give colour to the output operation'''
    header = '\033[95m'
    ok_blue = '\033[94m'
    ok_green = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'

    def disable(self):
        '''method used to disable the colors'''
        self.header = ''
        self.ok_blue = ''
        self.ok_green = ''
        self.warning = ''
        self.fail = ''
        self.endc = ''

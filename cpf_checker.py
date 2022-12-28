'''Module to filter CPFs from a given input file'''
class BColors:
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

class Messages:
    '''Messages used to log outputs'''
    VALID = BColors.ok_green + "[+] Valid CPF: "
    INVALID = BColors.fail + "[-] Invalid CPF: "
    FAILED_OPEN_FILE = BColors.fail + \
        "[E] Error while handling the file! \
        Check if you have the right permissions \
        to write in disk or if the file exists: \n"

class IOchecker:
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
        except Exception as exception:
            print(Messages.FAILED_OPEN_FILE + exception)
        return i_file

    def output_file(self, path, content):
        '''writes valid CPF's to an external file'''
        try:
            if not self.first_write:
                self.mode = "a"
            o_file = open(path, mode=self.mode, encoding="utf-8")
            o_file.write(content)
            self.first_write = False
        except Exception as exception:
            print(Messages.FAILED_OPEN_FILE + exception)
        return o_file

class FilterCPF:
    '''Call all the methods used to filter CPF'''
    io_obj = IOchecker("")
    def cpf_without_chars(self, cpf):
        '''removes "." and "-" from the cpf'''
        cpf = cpf.strip()
        filtered_cpf = ""
        for char in cpf:
            filtered_cpf += filtered_cpf.join(char.replace(".", "").replace("-", ""))
        return filtered_cpf

    def has_numbers_only(self, cpf):
        '''checks if the line contains digits only'''
        if self.cpf_without_chars(cpf).isdigit():
            return True
        return False

    def has_eleven_digits(self, cpf):
        '''verify if the line has 11 digits'''
        if len(self.cpf_without_chars(cpf)) == 11:
            return True
        return False

    def verify_first_digit(self, cpf):
        '''based on the CPF algorithm, it verifies the 1st verification digit'''
        # result from the multiplication of each digit from cpf times the iterator + its product
        sum_result = 0
        # Call the method to clean the CPF string and stores the returns value on cpf_without_chars
        cpf_without_chars = self.cpf_without_chars(cpf)

        if self.has_numbers_only(cpf_without_chars) and self.has_eleven_digits(cpf_without_chars):
            for counter, char in enumerate(str(cpf_without_chars)[::-1]):
                digit = int(char)
                # jumps the 2 verification digits, which has the 0 and 1 indexers
                if counter > 1:
                    sum_result = sum_result + (digit * counter)
                    return True
            if sum_result % 11 < 2 and int(cpf_without_chars[9]) == 0:
                return True
            if sum_result % 11 >= 2 and int(cpf_without_chars[9]) == (11 -(sum_result % 11)):
                return True
        return False

    def verify_second_digit(self, cpf):
        '''based on the CPF algorithm, it verifies the 2st verification digit'''
        # result from the multiplication of each digit from cpf times the iterator + its product
        sum_result = 0
        # Call the method to clean the CPF string and stores the returns value on cpf_without_chars
        cpf_without_chars = self.cpf_without_chars(cpf)
        # 10, 9, 8, 7, 6, 5, 4, 3, 2
        multiplication_iterator = 2

        if self.has_numbers_only(cpf_without_chars) and self.has_eleven_digits(cpf_without_chars):
            for counter, char in enumerate(str(cpf_without_chars)[::-1]):
                digit = int(char)
                # jumps the 1st verification digit, which has the 0 indexer
                if counter >= 1:
                    sum_result = sum_result + (digit * multiplication_iterator)
                    multiplication_iterator += 1

            if sum_result % 11 < 2 and int(cpf_without_chars[10]) == 0:
                return True
            if sum_result % 11 >= 2 and int(cpf_without_chars[10]) == (11 -(sum_result % 11)):
                return True
        return False

    def validate_algorithm(self, cpf):
        '''call both 1st and 2st verification digits methods'''
        if self.verify_first_digit(cpf) and self.verify_second_digit(cpf):
            print(Messages.VALID + str(cpf))
            self.io_obj.output_file("output_valid_cpfs.txt", str(cpf))
        else:
            print(Messages.INVALID + str(cpf))

    def main(self):
        '''where everything begins'''
        for cpf in self.io_obj.input_file("cpf_list.txt"):
            self.validate_algorithm(cpf)

obj = FilterCPF()
obj.main()

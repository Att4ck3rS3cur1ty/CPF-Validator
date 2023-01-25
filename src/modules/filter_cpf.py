'''Module to filter CPFs from a given input file'''
from in_out import IOchecker
from messages_validation import Messages
from statistics_ import Statistics

class FilterCPF:
    '''Call all the methods used to filter CPF'''
    io_obj = IOchecker("")
    statistics_obj = Statistics(0,0)
    messages_validation = Messages()

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

    def validate_algorithm(self, input_filename):
        '''call both 1st and 2st verification digits methods'''
        valid_cpf_counter = 0
        invalid_cpf_counter = 0
        for cpf in self.io_obj.input_file(input_filename):
            if self.verify_first_digit(cpf) and self.verify_second_digit(cpf):
                print(Messages.VALID + str(cpf))
                valid_cpf_counter += 1
                self.statistics_obj.set_amount_valid_cpf(valid_cpf_counter)
                self.io_obj.output_file("../../output_valid_cpfs.txt", str(cpf))
            else:
                invalid_cpf_counter += 1
                self.statistics_obj.set_amount_invalid_cpf(invalid_cpf_counter)
                print(Messages.INVALID + str(cpf))
        self.statistics_obj.average_filtered_cpf()

    def main(self):
        '''where everything begins'''
        self.validate_algorithm("../../cpf_list.txt")

obj = FilterCPF()
obj.main()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

class Messages:
    VALID = bcolors.OKGREEN + "[+] Valid CPF: "
    INVALID = bcolors.FAIL + "[-] Invalid CPF: "
    FAILED_OPEN_FILE = bcolors.FAIL + \
        "[E] Error while handling the file! \
        Check if you have the right permissions \
        to write in disk or if the file exists: \n"

class IOchecker:
    # initiates the variables
    def __init__(self, path):
        self.path = path

    # reads the input CPF list file 
    def inputFile(self, path):
        #with open(path, "r") as iFile:
        #    return iFile
        try:
            # with open(path, "r") as iFile:
            #    return iFile
            iFile = open(path, "r")
        except Exception as e:
            print(Messages.FAILED_OPEN_FILE + e)
        # finally:
        #    iFile.close()
        return iFile

    # writes to an external file the valid CPF's
    def outputFile(self, path, content):
        try:
            # with open(path, "w") as oFile:
            #    return oFile
            oFile = open(path, "w")
            oFile.write(content)
        except Exception as e:
            print(Messages.FAILED_OPEN_FILE + e)
        return oFile

class FilterCPF:
    io_obj = IOchecker("")
    # removes "." and "-" from the cpf
    def CPFWithoutChars(self, cpf):
        cpf = cpf.strip()
        filtered_cpf = ""
        for char in cpf:
            filtered_cpf += filtered_cpf.join(char.replace(".", "").replace("-", ""))
        return filtered_cpf

    def hasNumbersOnly(self, cpf):
        if self.CPFWithoutChars(cpf).isdigit(): return True

    def hasElevenDigits(self, cpf):
        if len(self.CPFWithoutChars(cpf)) == 11: return True

    def verifyFirstDigit(self, cpf):
        # result from the multiplication of each digit from cpf times the iterator + its product
        sum_result = 0
        # Call the method to clean the CPF string and stores the returns value on cpf_without_chars
        cpf_without_chars = self.CPFWithoutChars(cpf)
        
        if self.hasNumbersOnly(cpf_without_chars) and self.hasElevenDigits(cpf_without_chars):
            for counter, char in enumerate(str(cpf_without_chars)[::-1]):
                digit = int(char)
                # jumps the 2 verification digits, which has the 0 and 1 indexers
                if counter > 1:
                    sum_result = sum_result + (digit * counter)

            if sum_result % 11 < 2 and int(cpf_without_chars[9]) == 0:
                return True
            elif sum_result % 11 >= 2 and int(cpf_without_chars[9]) == (11 -(sum_result % 11)):
                return True
            else:
                return False
            
    def verifySecondDigit(self, cpf):
        # result from the multiplication of each digit from cpf times the iterator + its product
        sum_result = 0
        # Call the method to clean the CPF string and stores the returns value on cpf_without_chars
        cpf_without_chars = self.CPFWithoutChars(cpf)
        # 10, 9, 8, 7, 6, 5, 4, 3, 2
        multiplication_iterator = 2
        
        if self.hasNumbersOnly(cpf_without_chars) and self.hasElevenDigits(cpf_without_chars):
            for counter, char in enumerate(str(cpf_without_chars)[::-1]):
                digit = int(char)
                # jumps the 1st verification digit, which has the 0 indexer
                if counter >= 1:
                    sum_result = sum_result + (digit * multiplication_iterator)
                    multiplication_iterator += 1

            if sum_result % 11 < 2 and int(cpf_without_chars[10]) == 0:
                return True
            elif sum_result % 11 >= 2 and int(cpf_without_chars[10]) == (11 -(sum_result % 11)):
                return True
            else:
                return False

    def validateAlgorithm(self, cpf):
        if self.verifyFirstDigit(cpf) and self.verifySecondDigit(cpf):
            print(Messages.VALID + str(cpf))
            self.io_obj.outputFile("output_valid_cpfs.txt", str(cpf))
        else:
            print(Messages.INVALID + str(cpf))

    def main(self):
        for cpf in self.io_obj.inputFile("cpf_list.txt"):
                self.validateAlgorithm(cpf)

obj = FilterCPF()
obj.main()
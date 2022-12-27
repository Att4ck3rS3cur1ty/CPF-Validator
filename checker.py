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

class IOchecker:
    # initiates the variables
    def __init__(self, path):
        self.path = path

    # reads the input CPF list file 
    def inputFile(self, path):
        #with open(path, "r") as iFile:
        #    return iFile
        iFile = open(path)
        return iFile

    # writes to an external file the valid CPF's
    def outputFile(self, path):
        with open(path, "w") as oFile:
            return oFile

class FilterCPF:
    io_obj = IOchecker("")
    # removes "." and "-" from the cpf
    def CPFWithoutChars(self, cpf):
        filtered_cpf = ""
        for char in cpf:
            filtered_cpf += filtered_cpf.join(char.replace(".", "").replace("-", "")) # criar lista mesmo?
        filtered_cpf = filtered_cpf.strip()
        return filtered_cpf

    def hasNumbersOnly(self, cpf):
        if self.CPFWithoutChars(cpf).isdigit(): return True

    def hasElevenDigits(self, cpf):
        if len(self.CPFWithoutChars(cpf)) == 11: return True
            
    def validateAlgorithm(self, cpf):
        # 10, 9, 8, 7, 6, 5, 4, 3, 2
        multiplication_iterator = 2
        # result from the multiplication of each digit from cpf times the iterator + its product
        sum_result = 0
        cpf_without_chars = self.CPFWithoutChars(cpf)
        
        if self.hasNumbersOnly(cpf_without_chars) and self.hasElevenDigits(cpf_without_chars):
            for counter, char in enumerate(str(cpf_without_chars)[::-1]):
                digit = int(char)
                # jumps the 2 verification digits, which has the 0 and 1 indexes
                if counter > 1:
                    sum_result = sum_result + (digit * multiplication_iterator)
                    multiplication_iterator += multiplication_iterator

            if sum_result % 11 < 2 and str(cpf_without_chars[9] == 0) \
            or sum_result % 11 >= 2 and str(cpf_without_chars[9] == (11 -(sum_result % 11))):
                print(bcolors.OKGREEN + "[+] Ok! First digit from " + cpf_without_chars +" is valid.")
                # exit()
                return True
            else: 
                print(bcolors.FAIL + "[-] The first CPF's verification digit is invalid.")
                return False

    def main(self):
        for cpf in self.io_obj.inputFile("cpf_list.txt"):
                self.validateAlgorithm(cpf)

obj = FilterCPF()
obj.main()
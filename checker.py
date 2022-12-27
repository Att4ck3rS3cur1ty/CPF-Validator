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
        return filtered_cpf

    def hasNumbersOnly(self, cpf):
        if self.CPFWithoutChars(cpf).isdigit(): return True

    def hasElevenDigits(self, cpf):
        if len(self.CPFWithoutChars(cpf)) == 11: return True

    def validateAlgorithm(self, cpf):
        # 10, 9, 8, 7, 6, 5, 4, 3, 2
        multiplication_interator = 2
        # result from the multiplication of each digit from cpf times the iterator + its product
        sum_result = 0

        for counter, char in enumerate(str(self.CPFWithoutChars(cpf))[::-1]):
            if char is not "\n": digit = int(char)
            # jumps the 2 verification digits, which has the 0 and 1 indexes
            if counter > 1:
                sum_result = sum_result + (digit * multiplication_interator)
                multiplication_interator += multiplication_interator
        
        if sum_result % 11 < 2 and str(self.CPFWithoutChars(cpf)[10] != 0) \
        or sum_result % 11 >= 2 and str(self.CPFWithoutChars(cpf)[10] != (11 - sum_result % 11)):
            print(bcolors.FAIL + "[-] The first CPF'S verification digit is invalid. \nExiting.. ")
            # exit()
            return False

    def isValid(self):
        for cpf in self.io_obj.inputFile("cpf_list.txt"):
            if self.hasNumbersOnly and self.hasElevenDigits:
                print(bcolors.OKGREEN + "[+] CPF " + str(cpf.strip) + " has numbers only and eleven digits. Continuing!")
                self.validateAlgorithm(cpf)
            else:
                print(bcolors.FAIL + "[-] " + cpf + " is not valid. It has characters or more/less than 11 digits. \nExiting...")
                exit()

obj = FilterCPF()
obj.isValid()
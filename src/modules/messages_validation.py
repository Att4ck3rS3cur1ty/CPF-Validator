from colors import ByteColors

class Messages:
    '''Messages used to log outputs'''
    VALID = ByteColors.ok_green + "[+] Valid CPF: "
    INVALID = ByteColors.fail + "[-] Invalid CPF: "
    FAILED_OPEN_FILE = ByteColors.fail + \
        "[E] Error while handling the file! \
        Check if you have the right permissions \
        to write in disk or if the file exists: \n"
    AMOUNT_VALID = ByteColors.endc + "\n" + "Amount of valid CPFs: "
    AMOUNT_INVALID = ByteColors.endc + "Amount of invalid CPFs: "
    AVERAGE = ByteColors.endc + "Average: "

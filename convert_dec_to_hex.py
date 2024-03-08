# Convert decimal integers to hexadecimal strings
# Code for cousin's Allen Bradley PanelView and 17xx series PLC issue
# Old PLCs have hex and integer datatypes, but not strings.

def convert(num) -> str:
    if num > 255:
        raise Exception("Only works for error codes 0x00 to 0xFF")

    prefix = "0x" if num > 15 else "0x0"
    base = 16
    result = ""

    if num == 0:
        result = "0"

    while num > 0:
        remainder = num % base
        num = num // base
        result = lookup(remainder) + result

    return prefix + result


def lookup(num) -> str:
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    elif num == 2:
        return "2"
    elif num == 3:
        return "3"
    elif num == 4:
        return "4"
    elif num == 5:
        return "5"
    elif num == 6:
        return "6"
    elif num == 7:
        return "7"
    elif num == 8:
        return "8"
    elif num == 9:
        return "9"
    elif num == 10:
        return "A"
    elif num == 11:
        return "B"
    elif num == 12:
        return "C"
    elif num == 13:
        return "D"
    elif num == 14:
        return "E"
    elif num == 15:
        return "F"
    else:
        raise Exception("Invalid input")


if __name__ == '__main__':

    # num = 1044942
    # expected = "0x0000000FF1CE"
    # print(convert(num))
    #
    # num = 2343432205
    # expected = "0x8BADF00D"
    # print(convert(num))
    #
    # num = 3131746989
    # expected = "0xBAAAAAAD"
    # print(convert(num))
    #
    # num = 3203381950
    # expected = "0xBEEFBABE"
    # print(convert(num))
    #
    # num = 3405691582
    # expected = "0xCAFEBABE"
    # print(convert(num))

    for ii in range(256):
        print(convert(ii))


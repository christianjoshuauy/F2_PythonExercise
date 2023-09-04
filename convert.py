def decToBinary(dec):
    bin = ""
    if(dec == 0):
        return "0"
    while dec > 0:
        bin = str(dec % 2) + bin
        dec = int(dec / 2)  # also dec // 2
    return bin


def binaryToN(bin, type):
    ans = 0
    for digit in bin:
        ans = ans * 2 + int(digit)

    if type == 8:
        ans = decToOctal(ans)
    elif type == 16:
        ans = decToHex(ans)
    return ans


def decToOctal(dec):
    octal = ""
    if (dec == 0):
        return "0"
    while dec > 0:
        octal = str(dec % 8) + octal
        dec = int(dec / 8)  # also dec // 8
    return octal


def decToHex(dec):
    hex_digits = "0123456789ABCDEF"
    hex = ""
    if (dec == 0):
        return "0"
    while dec > 0:
        rem = dec % 16
        hex_digit = hex_digits[rem]
        hex = hex_digit + hex
        dec = int(dec / 16)  # also dec // 16
    return hex


def main():
    dec = int(input('Enter decimal: '))
    binary = input('Enter binary: ')
    n = int(input('Enter N type (8, 10, 16): '))
    print(f'Decimal to binary: {decToBinary(dec)}')
    print(f'Binary to N: {binaryToN(binary, n)}')
    print(f'Decimal to octal: {decToOctal(dec)}')
    print(f'Decimal to hexadecimal: {decToHex(dec)}')


main()
#convert hexadecimal to binary

HEX_TO_BINARY_CONVERSION_TABLE = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

def hex_to_binary(hex_string):
    bin_string = ''
    for i in hex_string:
        bin_rep = HEX_TO_BINARY_CONVERSION_TABLE[i]
        bin_string += bin_rep
    
    return bin_string

def main():
    number = 55683
    hex_number = hex(number)[2:]
    print(f'hex_number: {hex_number}')
    
    bin_number = hex_to_binary(hex_number)
    print(f'binary_number: {bin_number}')

    #int(. , 2) specifies that input is binary sting
    original_number = int(bin_number, 2)
    print(f'original_number: {original_number}')



if __name__ == '__main__':
    main()
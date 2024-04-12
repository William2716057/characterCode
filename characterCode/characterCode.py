def stringToIntArray(inputString): #converts to decimal
    int_array = []

    for char in inputString:
        charCode = ord(char)
        int_array.append(charCode)

    return int_array

def intToHex(int_array):
    hex_array = []

    for num in int_array:
        hex_representation = hex(num)[2:]  # Convert integer to hexadecimal, remove '0x' prefix
        hex_array.append(hex_representation)

    return hex_array

input_string = "abcdeABCDE"
result = stringToIntArray(input_string)
print(result)

hexResult = intToHex(result)
print(hexResult)
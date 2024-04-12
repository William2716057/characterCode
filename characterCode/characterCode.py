import base64

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

def int_array_to_base64(int_array):
    bytes_array = bytes(int_array)
    base64_string = base64.b64encode(bytes_array).decode('utf-8')
    return base64_string


input_string = "abcdeABCDE" #change string here
result = stringToIntArray(input_string)
print(result)

hexResult = intToHex(result)
print(hexResult)

base64_result = int_array_to_base64(result)
print(base64_result)




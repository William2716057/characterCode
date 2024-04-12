import base64

def stringToIntArray(inputString): #converts to decimal
    intArray = []

    for char in inputString:
        charCode = ord(char)
        intArray.append(charCode)

    return intArray

def intToHex(int_array):
    hex_array = []

    for num in int_array:
        hex_representation = hex(num)[2:]  # Convert integer to hexadecimal, remove '0x' prefix
        hex_array.append(hex_representation)

    return hex_array

def intTob64(int_array): #converts to base64
    byteArray = bytes(int_array)
    base64_string = base64.b64encode(byteArray).decode('utf-8')
    return base64_string

def intToOctal(int_array):
    octalArray = []

    for num in int_array:
        octalRepresentation = oct(num)[2:]  # Convert integer to octal and remove '0o' prefix
        octalArray.append(octalRepresentation)

    return octalArray

inputString = "abcdeABCDE" #change string here
result = stringToIntArray(inputString)
print(result)

hexResult = intToHex(result)
print(hexResult)

base64Result = intTob64(result)
print(base64Result)

octalResult = intToOctal(result)
print(octalResult)




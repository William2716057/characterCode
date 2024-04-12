import base64

def stringToIntArray(inputString): #converts to decimal
    intArray = []

    for char in inputString:
        charCode = ord(char)
        intArray.append(charCode)

    return intArray

def intToHex(int_array):
    hexArray = []

    for num in int_array:
        hexRepresentation = hex(num)[2:]  # Convert integer to hexadecimal, remove '0x' prefix
        hexArray.append(hexRepresentation)

    return hexArray

def intTob64(int_array): #converts to base64
    byteArray = bytes(int_array)
    base64_string = base64.b64encode(byteArray).decode('utf-8')
    return base64_string

def intToBinary(int_array):
    binaryArray = []

    for num in int_array:
        binaryRepresentation = bin(num)[2:]  # Convert integer to binary and remove '0b' prefix
        binaryArray.append(binaryRepresentation)

    return binaryArray

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

#here
binaryResult = intToBinary(result)
print(binaryResult)

octalResult = intToOctal(result)
print(octalResult)




import base64

def alphabetPos(text):
    result = []
    for char in text:
        if char.isalpha():

            if char.isupper():
                result.append(str(ord(char) - ord('A') + 1))
            else:
                result.append(str(ord(char) - ord('a') + 1))
    return ' '.join(result)

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

def intToB32(int_array):
    bytesArray = bytes(int_array)
    b32String = base64.b32encode(bytesArray).decode('utf-8')
    return b32String

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
print(alphabetPos(inputString))
result = stringToIntArray(inputString)
print(result)

hexResult = intToHex(result)
print(hexResult)

base32_result = intToB32(result)
print(base32_result)

base64Result = intTob64(result)
print(base64Result)

binaryResult = intToBinary(result)
print(binaryResult)

octalResult = intToOctal(result)
print(octalResult)




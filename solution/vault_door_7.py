import re;

def convert32BitsToArrayOf4_8bitsBinary(binary32Bit):
    array4_8bitBinary = [];
    for i in range(0, 32, 8):
        array4_8bitBinary.append(binary32Bit[i:i+8]);
    return array4_8bitBinary;

def convertArrayOfBinaryToASCII(binaryArray):
    plain_ascii = "";
    for binary in binaryArray:
        plain_ascii += chr(int(binary, 2));
    return plain_ascii;

# paste the return statement from the checkPassword function.
integer_array = '''        return x[0] == 1096770097
            && x[1] == 1952395366
            && x[2] == 1600270708
            && x[3] == 1601398833
            && x[4] == 1716808014
            && x[5] == 1734293296
            && x[6] == 842413104
            && x[7] == 1684157793;
'''
integer_array = integer_array.strip();

# extracting the integers using regex with integers having 2 or more digits.
integer_array = re.findall(r'\d{2,}', integer_array);

flag= "picoCTF{"

for integer in integer_array:
    bits = 32;
    # converting the integer to a 32 bit binary with leading 0
    binary_reprensentation = format(int(integer), f'0{bits}b');
    binary_array = convert32BitsToArrayOf4_8bitsBinary(binary_reprensentation);
    flag += convertArrayOfBinaryToASCII(binary_array);

flag += "}";

print(flag);
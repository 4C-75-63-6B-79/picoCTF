hexValue = ''' 0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d, 0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa, 0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27, 0xa , 0x66, 0x36, 0x30, 0x67, 0x6c, 0x64, 0x6c, '''

# hexValue = input('Paste the hex value you copied. Please remove the square brackets from the end and front and enter the value in single line. Or you can directly edit the code on your machine.')

hexValuelist = hexValue.split(",");
print(hexValuelist);

print('picoCTF{', end="");

for hexValue in hexValuelist:
    if(hexValue.strip() == ''):
        continue;
    print(chr(int(hexValue.strip(), 16) ^ int('0x55', 16)), end="");
print('}');
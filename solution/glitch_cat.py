import re

# 'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'

flag_string = input('enter the flag string you got form the webshell.');

hex_values = re.findall(r'0x([0-9]{2})', flag_string);

hex_string = "";

print("replace the corresponding hex values with the respective characters in the flag string .")

for hex_value in hex_values:
    print(hex_value, chr(int(hex_value, 16)))
    hex_string += chr(int(hex_value, 16));

print("hex value in string format", hex_string);

alphabets = 'abcdefghijklmnopqrstuvwxyz';

key = input('Enter the key');
encoded_flag = input("Enter the encoded flag");
decoded_flag = "";

for character in encoded_flag:
    if not character.isalpha():
        decoded_flag += character;
        continue;
    index = key.index(character.upper());
    if(character.isupper()):
        decoded_flag += alphabets[index].upper();
    else:
        decoded_flag += alphabets[index];

print(f'flag is {decoded_flag}');
import re

# Paste the if conditions here form the source.
verification_conditions = '''if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == '706c') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_b') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == '5}') {'''

order = re.findall(r'substring\((.{1,}),', verification_conditions); # extracting the start index from the substring function
flag_bits = re.findall(r'\'(.{1,})\'', verification_conditions); # extracting the string to which the equality is compared in the if conditions.

order_flag = {}

for i in range(len(flag_bits)):
    index = re.findall(r'([0-9]{1,})', order[i]); # since all the start index in substring have split*num. So here we are extracting the number here.
    if(len(index) == 0): # in case of split there is no number here so the index will be of len 0 we assign index 1 here
        index = 1;
    else:
        index = int(index[0])
    order_flag[index] = flag_bits[i];

print('flag bits in unorderd way: ', order_flag);

for i in range(len(order_flag)):
    print(order_flag[i], end="");
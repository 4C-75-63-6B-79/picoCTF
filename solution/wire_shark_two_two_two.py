import re

file = open('solution/flags.txt', 'r');
file_text = str(file.readlines());

flags = re.findall(r'(picoCTF\{.{1,64}\})', file_text);

for flag in flags:
    print(flag)



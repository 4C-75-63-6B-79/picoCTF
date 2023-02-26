import base64

st = input('Enter the encoded string from the problem: ');

print(base64.b64decode(st));
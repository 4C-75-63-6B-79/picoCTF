import base64

def base64decode(base64_encoded):
    try:
        return base64.b64decode(base64_encoded);
    except:
        return False;

base64_encoded_password = input('Enter the base64 encoded password fomr the indexjs file: ');

did_base64_decode_success = base64decode(base64_encoded_password);

while(did_base64_decode_success == False):
    base64_encoded_password += '=';
    did_base64_decode_success = base64decode(base64_encoded_password);

print(base64decode(base64_encoded_password));
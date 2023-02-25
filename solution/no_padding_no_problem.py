import binascii

# not actual encoding process but what I described in the readme
def encodeInRSA():
    text = 'picoCTF{'

    while(len(text) != 153):
        text += ' ';

    text += '}';

    print('length of the text', len(text));

    byte_text = text.encode(encoding='utf-8');
    print('text as byte string', byte_text);

    hex_text = binascii.hexlify(byte_text);
    print('text in hex format', binascii.hexlify(hex_text));

    decimal_text = int(hex_text, 16);
    print('text in decimal format', decimal_text);

    encrypted_text = pow(decimal_text, e, n);
    print('text in it\'s encrypted format', encrypted_text);

    print('length of the encrypted text is ', len(str(encrypted_text)));

# this function findPowerOf2 find the times 2 should be raised to get the number which is provided as function parameter
def findPowerOf2(number):
    d = 0;
    while(number > 1):
        if(number % 2 != 0):
            return False;
        d += 1;
        number = number // 2;
    return d;

n = 117565895843055422729774663458742764196973201067768124260054900592712017215351167362398067390316132225448176067370864455694851720545500517747714312752663576820720993229790592827503073277524098499870411040856612643417026603926672607513484703890348176085923528930924906959991013022767993668786709680430045086919
e = 65537
cipher_text = 2082596883884155007923567360359818901217638350318930858897551861382398586780609960620048185130551805940498617066697687370882523452693721578517456776457027740266962449119512627742756815821888118124282549895502868504360418907010522271664892491422020631903423301634058676777070711840993608306088581890847908510
decrypted_text_02 = 50840468978604254774626166524264148597196467438551937270038715363764772532954456380757080375382991237539598460905004251731319768386332899266256890483711348199596840946183407096664690841890422127801229845420813275048514788944029459584705236168528219581233140619566277423407465341261603912343738455492123129695


print('length of n', len(str(n)))
print('length of cipher text', len(str(cipher_text)))

# encoding the text 'picoCTF{'
# encodeInRSA();

d=1;

# Do not run this loop takes a long time and it might work or it might not work. Did not work for me.
# while decrypted_text_02 != pow(2, d, n):
#     d += 1;
#     print(d);

# The final solution
cPlusN = cipher_text + n;
decrypted_cPlusN = 290275030195850039473456618367455885069965748851278076756743720446703314517401359267322769037469251445384354856017744835453

st = "{:x}".format(decrypted_cPlusN);
print(st);
print(binascii.unhexlify(st));




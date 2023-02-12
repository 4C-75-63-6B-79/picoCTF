# ceaser ciper thing

# use wire shark to open the pcapng file and then (used internet help her ) use file export object and choose tftp
# save all the 6 files
# first file is instruction txt had ceser_cipher with key 13 so did that with this scricpt
# got this TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
# which is TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN
# now opened the file in the notepad found some text just again ran the ceaser cipher on it 13 was the key
# got this IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
# which is I USED THE PROGRAM AND HID IT WITH - DUE DILIGENCE. CHECKOUT THE PHOTOS
# opened archive of program.deb using 7 zip the saw a lot of steghid and a readme on it
# googled it to find it is a program to hide date in files
# installed in on wsl using sudo apt-get install steghide
# use the command steghide --extract -sf picture3.bmp with parapharase DUEDILIGENCE
# got the hint from a ctf write up
# got flag.txt
# flag = picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}


def rotateAlpha(letter, key, start):
    asciiVal = ord(letter);
    rotVal = ((asciiVal + key - start) % 26);
    if(rotVal == 0):
        rotVal = 26;
    return chr(start+rotVal);

def rotateString(word, key):
    result = '';
    key = key % 26;
    for i in word:
        asciiVal = ord(i);
        if( 65 <= asciiVal <= 90):
            result = result + rotateAlpha(i, key, 64);
        elif( 97 <= asciiVal <= 122):
            result = result + rotateAlpha(i, key, 96);
        else:
            result = result + i;
    
    return result;


word = input('Enter the word to decipher');
print(word)
for i in range(1,27):
    print('value of key', i);
    print('decipher text', rotateString(word, i));


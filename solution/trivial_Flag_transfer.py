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


# rotates a single letter
def rotAlpha(alpha, key, start):
	return chr(start + ((ord(alpha) - start + key)%26))

# rotates and returns the entire word as string
def rotateWord(word, key):
	rotatedWord = ''
	for i in word:
		if 65 <= ord(i) <= 90:
			rotatedWord += rotAlpha(i, key, 65)
		elif 97 <= ord(i) <= 122:
			rotatedWord += rotAlpha(i, key, 97)
		else:
			rotatedWord += i
	return(rotatedWord)
	
	
def printAllCipher(word):
	for i in range(26):
		print("key:", i, rotateWord(word, i))

word = ''
print('Enter 0 to end the program.')

# loops take input until user enter 0
while not (word == '0'):
	word = input('Enter word to be deciphered: ')
	if(word == '0'):
		print('program exit');
		break
	printAllCipher(word)


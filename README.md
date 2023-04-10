# picoCTF

<details>
<summary> Mini Rsa </summary>

### Mini Rsa
- We know that e is small.
- So what we can do here is we can multiply n with integers and add c to the product like this n * i + c where i is (0,1,2,3,4....).
- Then what we can do is find the  eth root of the obatined value.
- We can then convert the eth root to hex value and see if the hex value of pico which is 7069636f is present in that if yes then we convert that to plain text.
#### Program Description
- The written [python program](./solution/mini_rsa.py) to find deciphered text.
- Functions nth_power and the nth_pow helps us to find the root. Both functions do the same thing but the nth_power takes less time as it calculates a better value for the lower limit.
- Both functions use binary search to find the root you can google it.
- To use [this](./solution/mini_rsa.py) solution just paste the value of your n, c and e value in the lower given variables and run it. 
- After runnig it please be patient it takes **Few Seconds to Print the result**.
- This solution worked for me but it might not for you because I might have made some mistake so sorry.
- flag: picoCTF{e_sh0u1d_b3_lArg3r_85d643d5}
</details>

<details>
<summary>Dachshund Attacks</summary>

### Dachshund Attacks
- To make this solution in used various resources.
- I read this wikipedia page about **[Wiener Attacks](https://en.wikipedia.org/wiki/Wiener%27s_attack)** which is the photo hint.
- To get a better understanding about how this works I saw this [video](https://www.youtube.com/watch?v=OpPrrndyYNU).
- After that I studied about what are continued fractions from this wikipedia page **[Continued Fractions](https://en.wikipedia.org/wiki/Continued_fraction#:~:text=In%20mathematics%2C%20a%20continued%20fraction,another%20reciprocal%2C%20and%20so%20on)**.
#### Program Description
- After doing the above I wrote this [python program](./solution/Dachshund_Attacks.py) to find the d values using the above [video](https://www.youtube.com/watch?v=OpPrrndyYNU&t=613s) method.
- I wrote my own solution because I was not able to use the other mentioned methods for weiner attacks on web. 
- The findConvergent methods takes in a array of all the continued fractions and gives the value of single convergent.
- The getContinuedFraction function takes a N and e value and empty array and then find all the continued fractions value and returns array with all the continued fractions.
- The getAllConvergent function loops throught the entire continued fraction array and finds all the convergents
- Then we use for loop to loop through all the value of convergents and find the k / d values.
- We ignore the values of d which are even or don't give us a whole value of the fiN = (ed -1) / k
- And the we use the quadratic equation to find the p and q values as mentioned in the [video](https://www.youtube.com/watch?v=OpPrrndyYNU&t=298s).
- To get this working paste your n, c, e value in the variables from the webshell on picoCTF website and then run it.
- This worked for me and it might not work for you because there might be some mistake i made in this so sorry.
- flag: picoCTF{proving_wiener_3899149}
</details>

<details>
<summary>Trivial Flag Transfer</summary>

### Trivial Flag Transfer
- To solve this I googled how to open the pcapng file using wire shark.
- Use wire shark to open the pcapng file and then (used internet help her ) use file > export > object > tftp to get the files.
- Save all the 6 files.
- First file is instruction txt had ceser_cipher with key 13 so did that with this [python program](./solution/trivial_Flag_transfer.py).
- Got this after pasting the contents of the instructions file TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
- The above decipherd text read as TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN.
- Then I opened the plan file in the notepad found some text just again ran the ceaser cipher on it. 13 was the key.
- Got this IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
- Which reads as I USED THE PROGRAM AND HID IT WITH - DUE DILIGENCE. CHECKOUT THE PHOTOS
- Opened archive of program.deb using 7 zip the saw a lot of steghid and a readme on it.
- Googled it to find it is a program to hide date in files.
- Installed steghide on wsl using sudo apt-get install steghide.
- Used the command steghide --extract -sf picture3.bmp  given in the readme in archive. 
- Then got error. Googled to find that we need to use a parapharase. With further googling found that paraphrase is  DUEDILIGENCE.
- Got paraphrase hint from a ctf write up.
- Got flag.txt.
- flag: picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
</details>

<details>
<summary>More Cookies</summary>

### More Cookies
- Looking at the title which is cookies opened the developer tools > applications > cookies 
- Saw a long text thing in value which looked like base64. Tried converting it ascii. It was all gibberish.
- Ran Ceaser Cipher([here](./solution/trivial_Flag_transfer.py)) on it nothing happened just gibberish.
- Looked up the first hint which is **[Homomorphic encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption)**.
- This encryption is such that we can do operations on the encrypted form of data. The result of the operation is also encrypted. When this result is decrypted it is same as if the operation is performed on the decrypted original data.
- Googled 'Homomorphic encryption + cookies' found a ctf writeup which mentioned that there are words which capital letters in the problem description Cookies, Be Client. It also mentioned about CBC bit flip.
- Googled what is CBC. Watched this example of CBC encryption [video](https://www.youtube.com/watch?v=_aZQFXnnoO4). Got the basic understanding of what we do in CBC.
- Watched one more [video](https://www.youtube.com/watch?v=Rk0NIQfEXBA). Understood that CBC is a mode of operation. Other modes of operation are EBC and Conter mode.
- Google CBC bit flip. Read this [article](https://bernardoamc.com/cbc-bitflipping-attack/#:~:text=Bitflipping%20Attack,in%20the%20next%20ciphertext%20block.) and [this](https://resources.infosecinstitute.com/topic/cbc-byte-flipping-attack-101-approach/). Both have examples describing what happens in bitflip attack but I did not understand either of them.
- Read [this](https://github.com/HHousen/PicoCTF-2021/tree/master/Web%20Exploitation/More%20Cookies) and got the understanding why we are trying to CBC bit flip attack. This writeup suggested to read this [article](https://crypto.stackexchange.com/questions/66085/bit-flipping-attack-on-cbc-mode/66086#66086) which explain in detail what happens in CBC bit flip attack.
- Then I copied the code and tried to make it run and understand what the code is doing.
- Watched this [video](https://www.youtube.com/watch?v=i9KiOjeE-VY) and followed his solution.
- The problem was that running for the 0th postion was taking a long time and also connection was timing out.
- So I increased the char_postion to 12 seeing that the solution is at 13 postion.
- flag: picoCTF{cO0ki3s_yum_82f39377}
</details>

<details>
<summary>where are the robots?</summary>

### Where are the robots
- Doing the usual inspection of the source style thing in the dev tools.
- In cookies found things looking like base64 encoded.
- Nothing useful in the decoded base64.
- Looked the hint understood nothing.
- Googled about the challenge. Found that we need to find the **robots.txt** file.
- **Robots.txt** file tells search engine web crawlers to not index the page that are not meant for public view.
- Watched this [video](https://www.youtube.com/watch?v=pdMMq64D0OU).
- type "robots.txt" the url of the challenge website.
- get .html link paste that in the place of robots.txt in the url
- flag: picoCTF{ca1cu1at1ng_Mach1n3s_1bb4c}
</details>

<details>
<summary>No Padding, No Problem</summary>

### No Padding, No Problem

#### Wrong Approach
- First thing I did was to go back to [mini_rsa.py](/solution/mini_rsa.py) file and then read the personal notes to get a idea of how to encode a text using RSA.
- Since we have n and e so we can encode the text. Since in the challenge it is mentioned that no padding which might mean that the text is encoded as it is.
- From [mini_rsa](/solution/mini_rsa.py) we know that the length of the ciphered text is double of the deciphered text.
- We know that the total length of the ciphered text in this problem is 308 so the length of the deciphered text may be 308 / 2 = 154.  
- So we are going to take the text 'picoCTF{' and add bunch of space (ASCII = 32) so that the length of the string to be encoded is 153 and then at the end we will add }. The process of the encoding can be seen in [no_padding_no_problem.py](/solution/no_padding_no_problem.py) in function encodeInRsa.
- What ever you read above is not true since the length of the cipher text is reduced to 307 as seen when the program ran.

#### Correct Approach
- What I did not see that we can give it the ciphered text to decrypt?
- So I gave it 0 and 1. I would have raised it to power d but the answer would have been 0 and 1 respectively. 
- When entered 2 it returned a decrypted_value. Since we have n and the decryption of the 2, we might be able to find the d. decrypted_value = (2 ** d) % n.
- The d value can be found using two approach described below.
- Created a function findPowerOf2 in [no_padding_no_problem.py](/solution/no_padding_no_problem.py) that take in a number and returns the value of the power to which 2 should be raised to get that number.
- Or can directly run a while loop raising 2 to power 1,2,3.. and so on and mod with n till we get the decrypted_value when we enter 2. Tried this uptil 1500000.
- I tried both of the 2 ways but even after large number of iterations no answer was coming. 
- Googled about the problem.
- Read [this](https://ctftime.org/writeup/32010) solution which suggested to give the program to decrypt c+n value. I did not understand why this will work.
- Then read [this](https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/No_Padding_No_Problem.md) solution which mentioned that the unpadded RSA is homomorphic which we have read about in the the **More Cookies** challenge.
- Homomorphic encryption is such that when any operation is performed on the encrypted text and then if this is decrypted it will be same as if the operation is performed on the decrypted text.
- And on reading the [second](https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/No_Padding_No_Problem.md) solution we see how the use the homomorphic property.
- Used the first solution to get the result. I did not understand why the first method works.
- flag: picoCTF{m4yb3_Th0se_m3s54g3s_4r3_difurrent_0801973}
</details>

<details>
<summary>Vault Door 1</summary>

### Vault Door 1
- On reading the program understood that if I enter a password with length less than 8 the program will break, since it is taking the substring of password from letter 8.
- On examining the checkPassword function we can put all the letter in the respective index position to obtain the thing which is probably the flag.
- I wrote this small [python program](/solution/vault_door_1.py) to obtain the flag. I am sorry if I did not use the regular expression correctly.
- flag: picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_f6daf4}
</details>

<details>
<summary>Strings It</summary>

### Strings It
- Downloaded the file and opened it online [hex editor](https://hexed.it/). Saw that it is a elf file.
- The problem mentioned to not run the file. I don't know how to run the file.
- Looked at the hint. Hint opens a page to the strings command. 
- Run the strings command on the strings file. See a lot of lines of string that look like base 64 encoded. Try to decode a few using copy paste and python. Get error incorrect padding.
- Used the strings command on the strings file and created the file.txt out of the output of the strings command. strings strings >> file.txt.
- Opened the file.txt in nano and tried to ctrl + w to find the picoCTF. But doing this on the browser shell closed the window.
- So googled about the challenge and found we can use command grep to find the picoCTF in the file.txt.
- command cat file.txt | grep picoCTF
- flag: picoCTF{5tRIng5_1T_7f766a23}
</details>

<details>
<summary>Easy 1</summary>

### Easy 1
- wget the table.
- Encrypted flag: UFJKXQZQUNB key: SOLVECRYPTO
- Google about the one time pad. Read the [wikipedia article](https://en.wikipedia.org/wiki/One-time_pad) on it mainly the example section.
- When you read the example you will get the idea of how to decrypt the flag.
- I made this small [program](/solution/easy_1.py) to decrypt flag. You just have to enter the encrypted flag and the key when you run the program.
- flag: picoCTF{cryptoisfun}
</details>

<details>
<summary>logon</summary>

### logon
- Logged in using joe. Did not enter the password. Success you have logged in but no flag happened.
- Logged in as joe using password as password. Success you have logged in but no flag happened.
- Looked at the cookies. Saw cookies admin, username, password, __cf_bm, PHPSESSID.
- __cf_bm is something related to bots and PHPSESSID is some kind of session id.
- admin was false. Tried setting it to true. Nothing useful happened.
- Looked at the hint. 
- Logged in as human with password as password. Success you have logged in but no flag happened.
- Then realized if the joe is case sensitive. Logged in as Joe with no password gave an error "I'm sorry Joe's password is super secure. You're not getting in that way.
"
- Tried logging in as Joe this time with password as password. Same above error.
- Logged in as human and then clicked home and then tried logging in as Joe smae as above error.
- Googled about the problem.
- Saw this [video](https://www.youtube.com/watch?v=6IHI0teB7ek). Realized that what I did with the admin cookie previously was correct what I did wrong was not make T capital in True.
- flag: picoCTF{th3_c0nsp1r4cy_l1v3s_0c98aacc}
</details>

<details>
<summary>13</summary>

### 13
- This might be a ceaser cipher with key 13.
- Used the [trival_flag_transfer.py](./solution/trivial_Flag_transfer.py) program as there is ceaser cipher in there.
- The program will print the decipherd text for all the 26 key. The key here is most probably 13.
- flag: picoCTF{not_too_bad_of_a_problem}
</details>

<details>
<summary>caesar</summary>

### Caesar
- Here we are given a message in it's encrypted form. 
- Tried ceaser cipher on it using the [trival_flag_transfer.py](/solution/trivial_Flag_transfer.py)
- Got all the 26 rotations. Tried looking through them if any of then are meaningful phrases.
- This phrase looked meaningful "crossingtherubicondjneoach".
- Submitted it and it was the flag.
- flag: picoCTF{crossingtherubicondjneoach}
</details>

<details>
<summary>dont-use-client-side</summary>

### dont-use-client-side
- Opened the link and went to source.
- Saw that the password verfication was done in function veify. 
- And there was the flag in some form of jumbled form.
- verify function was selecting the element with id pass and getting it's value.
- Then it was checking if the substring 0 to 4 is pico. It is at a single time checking 4 characters. And similary if we calculate the value of the start and end in substring we can piece together the flag.
- We can look at the start index of the substring method in order of 0, split, split*2, split*3 and so on. And then put the value to which these substring are compared in order to get the flag.
- Or you can also use this [program](./solution/dont_use_client_side.py) to piece the flag together. All you have to do is paste in all the if conditions in the verify function in the source. If the program does not work for you sorry.
- Sorry if used something in the regex worngly.
- flag: picoCTF{no_clients_plz_b706c5}
</details>

<details>
<summary>Bases</summary>

### Bases
- Looking at the string in the problem description. It looks like base64 encoded.
- One can use this [program](./solution/bases.py) or [this online base 64 decoder](https://www.base64decode.org/) to decode the string.
- Just run the program and enter the encoded string and output is the flag value.
- picoCTF{l3arn_th3_r0p35}
</details>

<details>
<summary>First Grep</summary>

### First grep
- I have already read about this command while doing the previous problems.
- I helps us to find the patterns in files. I can do a lot more but I know only the basic stuff about it.
- One can read about grep by typing **man grep** in webshell.
- Typed this in webshell **grep picoCTF file**.
- flag: picoCTF{grep_is_good_to_find_things_5af9d829}
</details>

<details>
<summary>Pixelated</summary>

### Pixelated
- Downloaded the 2 images on to my computer looked at them both were like noise on old TV Screen but coloured.
- Looked at their size on disk but it was not large so no nothing in the zip format stored in them.
- Looked at the first hint which ahd a link to wikipedia article on [Visual Cryptography](https://en.wikipedia.org/wiki/Visual_cryptography). Read it.
- In the example section the article talks about how we can change the pixel values so that when the 2 images are stacked on top of each other we will get the original image.
- Looked at the second hint which also talked about stacking the 2 images.
- Tried to stack images using gimp and playing with different modes. Nothing useful happened.
- Google about the problem. Found [this](https://picoctf2021.haydenhousen.com/cryptography/pixelated) writeup which had [this](https://github.com/HHousen/PicoCTF-2021/blob/master/Cryptography/Pixelated/script.py) script. 
- The above script was using some libraries I did not understand what those libraries were doing.
- Watched [video](https://www.youtube.com/watch?v=e7Yx2nxGcqU) on the problem. What we actually have to do is to add the 2 images. Like add the red, blues and greens. Same as the wikipedia article but it was with black and white.
- I have read about manipulating images in the book **Automate the boring stuff with python** in [chapter 19](https://automatetheboringstuff.com/2e/chapter19/). So I went there to refresh a few things.
- After reading the chapter 19 created the [program](/solution/pixelated.py) to get the flag. Before running the program make sure that you have pillow module installed on your system.
- In the program we are using the module pillow about which you can find more at [here](https://pypi.org/project/Pillow/).
- flag: picoCTF{da8fcef8}
</details>

<details>
<summary>It is my Birthday</summary>

### It is my Birthday
- Opened the website went straight to the cookies section.
- Uploaded a single file gave error file too large.
- Uploaded no file and gave error no file.
- Created a file with 1 as the content and uploaded same in both gave error files are not different and no change in the cookie.
- Created another file with 2 as the content and uploader 1 in first and 2 in the other and gave error MD5 don't match.
- Added a invisible space to the pdf as content 1 got same error MD5 hashes don't match.
- Googled the MD5 hashes of pdf. Read [this](https://cs.indstate.edu/~fsagar/doc/paper.pdf).
- MD5 hashes is used to verify the file downloaded from server is same or not. This is done by creating MD5 on the server and then when file is downloaded if both are same then file is ok. 
- MD5 is not collision free which means that for two different inputs we can have same output.
- So our objective is to have 2 pdfs whoes MD5 hashes are same but they are different in some way. To have same md5 hashes we must some how use the collision thing.
- Since I have no idea on how to make pdf which are different but have same MD5 hashes I looked the hints.
- Hints mentioned to look at the category of the problem which is Web Exploitation and the second one said how many PHP sites check the rule in description. I did not understood anything from the hints.
- Googled how to make 2 pdf files with same md5 Hashes. Did not find a way to make such file.
- Then googled 2 files which have same md5 hash. Found [this](https://security.stackexchange.com/questions/21081/program-binaries-or-files-with-same-md5-hash) which has a link to [this](https://www.mathstat.dal.ca/~selinger/md5collision/) which had [link](http://web.archive.org/web/20071226014140/http://www.cits.rub.de/MD5Collisions/) to [script1](http://web.archive.org/web/20071226014140/http://www.cits.rub.de/imperia/md/content/magnus/letter_of_rec.ps) and [script2](http://web.archive.org/web/20071226014140/http://www.cits.rub.de/imperia/md/content/magnus/order.ps) with same MD5 hashes.
- I renamed those 2 files extentions to pdf.
- It worked and opened some program which had the flag.
- flag: picoCTF{c0ngr4ts_u_r_1nv1t3d_40d81ca2}
</details>
<details>
<summary>Wireshark twoo twooo two twoo...</summary>

### Wireshark twoo twooo two twoo...
- Downloaded the file onto my computer and opened it with wire shark
- Tried file > export Objects > TFTP. Nothing to export there.
- After looking here and there looked at the hints.
- Hint1: did you really find_the_flag? Looked for the find in the filter option. 
- Hint2: Look for traffic that seems suspicious.
- I don't know how to look for suspicios traffic. There was one thing highlighted in red. I did not understand what is inside it and there was no flag. 
- On scrolling down found another red highlighted thing.
- More scrolling found a request with GET method for flag in Frame 3320. Opened it nothing inside it useful.
- Since this is get request there must be a response. Careful looking under saw HTTP response with 200 status on frame 3329. It had text by side of it.
- Opened it to find the flag picoCTF{89d93dbb96a3857ac87ba0cea3c10a9e4c7b34d79b2edb463cef030d34297bd0}. Submitted it and found it was not correct.
- Looked further. And found there are many such request. There must be some way to filter these requests.
- Sorted the length. A bunch of response had 263 length. All had flags in them. It also had a red highlighted one in them which had a text/plain beside. 
- Text inside it was inform of base64 encoded. AQAAANdL16XINqtaIfPEd4oSsoqp95pLlVW4Iavm0x93mlJlUw-LqQ==/. Got error on decoding it.
- Copied the last flag picoCTF{3fe0b2788f30d9cb9f77d3b2752f13c554fe7f0e7a2883e57c8a44b34f35675c}. In correct.
- Googled how to filter the request and get the line based text. Filter data-text-lines containes "picoCTF".
- Then I exported the flags. file > export packet disections > as plain text.
- The wrote [this](/solution/wire_shark_two_two_two.py) to get all the flags. 
  - picoCTF{bfe48e8500c454d647c55a4471985e776a07b26cba64526713f43758599aa98b}
  - picoCTF{bda69bdf8f570a9aaab0e4108a0fa5f64cb26ba7d2269bb63f68af5d98b98245}
  - picoCTF{fe83bcb6cfd43d3b79392f6a4232685f6ed4e7a789c2ce559cf3c1ab6adbe34b}
  - picoCTF{711d3893d90f100c15e10ef4842abeed3a830f8237c1257cd47389646da97810}
  - picoCTF{3cf1e22d489fcfb6bb312a34f46c8699989ed043406134331452d11ce73cd59e}
  - picoCTF{b4cc138bb0f7f9da7e35085e349555aa6d00bdca3b021c1fe8663c0a422ce0d7}
  - picoCTF{41b8a1a796bd8d202016f75bc5b38889e9ea06007e6b22fc856d380fb7573133}
  - picoCTF{9812bc4be04e6f9c803152313db3da53b3dfb799bdb05aac46fa0dd0045d2fc2}
  - picoCTF{64cf3ede3736a340fdf2954be5151ce53bec291c5e48cbccb44faa529946e249}
  - picoCTF{c50d259a4e172fcb2eddbabeebd272473e4882b76c9efcd12c03ac04429d884a}
  - picoCTF{0a024b7d39603756feafa2bbaa1603b14a99eae5dcd59f1d957f511d822c8c06}
  - picoCTF{97211eec9228bb247d762527bace8b3e4ec2110c8834af12aefd3c552cdc21b2}
  - picoCTF{29679910c47d8afc737a1c21d7bf758cd3d81001bdbeec8c6f81a6ad88fdc279}
  - picoCTF{996979e9540be0fe9320e80eb6336047f8140a80830700907b99741310acf08f}
  - picoCTF{8b272a18c1005c95a420d4a0df426cb8441d29eb96210493a96fa25ac5e657aa}
  - picoCTF{e1d0a752dc71121200f4bcb1b8cc2e03e84488df229b82196afbe0045ef025c4}
  - picoCTF{0ba511844a2ab38fe0709bcdb2b8bdfeb37a0b466dc902e92062db4c2b3f455c}
  - picoCTF{dadda48e855421e14597ffc727943b57efd8c9a15d10bfd491f0390659162fb1}
  - picoCTF{f4dd87795395c74f3083f8caa4ec22d1531281554a6003d1c47c5f0370984ab6}
  - picoCTF{0f30a584680db9e70c7e1c6ca954c2f023b77f3fd2b05bd9aeee6e00dc4da5d7}
  - picoCTF{715e4d0d167e862af8825f62d3f4ff8aef20443445a06b1c68572390a2825d29}
  - picoCTF{7654ee03f31576e8ed44799fc4fa5ee053d35050000502e878d1fb8022618923}
  - picoCTF{068606b5faca0491d97a2b46fdca7f6f81acbd909ce691077fe77e03a3c0939a}
  - picoCTF{64ab681ffed33c49b5e8ae0576e22857e9a10ae30cdbee415fb514b84aa58aea}
  - picoCTF{8ae3995e726f8f2c3724e2e0522f038aba6649facd378d8965c648233d79a252}
  - picoCTF{1c125d267b5811cd25cca2d517e022270aa60f3c8461f4097c685bcca637a6a9}
  - picoCTF{824c298d14e1fe369df991af72ab0725d2e7c7d05b9655486873ccc467f4bd6b}
  - picoCTF{e1d8dd1b73d5fd7704a16c924ddee69dc6bf9beef14cc3a10142704b81f0fa07}
  - picoCTF{82d260fe0670d551347b164c54183d996c52ebeebb1ccfcc2c2ebb91268dc944}
  - picoCTF{74876fc61ebc9c902f8983979cd4c21206c69a23f0dcc0817e150dd75e446838}
  - picoCTF{49c52d1f30973f90716bbcbe3633e11cf70b9a31ed785871ccb80473302a59db}
  - picoCTF{89d93dbb96a3857ac87ba0cea3c10a9e4c7b34d79b2edb463cef030d34297bd0}
  - picoCTF{5ceacdce54c13a3fddfcfb225a00247304fbb15f29f9c90434383f277567992d}
  - picoCTF{c22a40a43ed7034bd935805f59603a46d3a1f2d6b8e31281eb0721597b6c6d62}
  - picoCTF{6071bca5da06d4f975a52357cda0cd6f0614787c1c70b1b7e1af2c7fb272d281}
  - picoCTF{65a8b141f019506feea38a119988ad645bcab1a5fa8693efdf26e1fd3cb44b4c}
  - picoCTF{d7f5cb78a895d3805601522b95d599cb6d2689c6a856e3fbee6aac2fca0c20f3}
  - picoCTF{739bb0f0aa17331819a0e942d37bfee757c8d9cd089cdfe32509027b92485213}
  - picoCTF{7a891e2c4ad0da374bc15ad7ad0ee081077dd376f06152781f780c201691713d}
  - picoCTF{a97d3ee943221888bd1157429e4a00ed5e9905a610e64664f7e36c7f5e0a4ef9}
  - picoCTF{c38d2d74dc21bbb2e3a95b52e2354ee523379cfe4f8b348c9c5b5d7bd7cb871b}
  - picoCTF{e4dc886c39a53ff118bf29041067cde48dcebb89b3dae61a8aba6187d671999a}
  - picoCTF{9fbd0d18aa1abfd289ba977ae4354b821cc74591260889afba1b0b6e7763aa31}
  - picoCTF{3fc0801bcd36336a2c030c6e5f452f5795be1d562e00411365fb64c6a2f688ef}
  - picoCTF{4aa86643eb2ddb5709725344cd0e63e6c52e35c2e64a39f3a4a0ee7bbd5d3ade}
  - picoCTF{4af8df415d17e6df99a5efddebcb33a68c0c8bf26d481eed16b5f77675030d7f}
  - picoCTF{e4f52a0d2a924906ac102a32c52ab9128bf9cd6e5294518ad3ed6748f853b0ab}
  - picoCTF{cc104e74a9f50164ee5652d168ef38a21b7a2d5e3196062e669e3a2705f1a0d3}
  - picoCTF{2aac620b0bdd2e6946d62c5d232ca32ba1f5a9d8ec82c060778b54ffeb8fbd1f}
  - picoCTF{4e55be07159def207afc142954f5673a0651d5f32f5f4090fb774d960628e352}
  - picoCTF{983e5e2703a132a49479e438bfba15ee5d02345b03d410b8163b685973937da7}
  - picoCTF{d342a46e8179de9941720c5e0eeac0d0fae9d3014d2ddcf531a7865a997b00e5}
  - picoCTF{2133904cfe757bc6c68c3e5f3749b37d67d7fa6ffb2768410be593d3fe8c4bd4}
  - picoCTF{29b726b9a57d176e1487d159474ee7e6508b66c05c526a00c942a8cebb6bb496}
  - picoCTF{7302b0dca07cd890c75e38d78d7e74d7bbf2b932f555aaf5b6754f56e778e3fc}
  - picoCTF{22e018bb8282e9d7852ed4e65f70a26524dabef78cf41e1db45c070c94621c57}
  - picoCTF{40f366ccf0f6462f5b8b1dc4d7384a62aa95565afcaad96a937b8c1f1134099b}
  - picoCTF{db38cbc215cde0d9cd52cbca2390defdb54303e998019a5c4ddaf9861b54efcb}
  - picoCTF{090fa8ec995ab9fc9f97cbe9ea36cb81c4504a3ca02466ddd207cfe7f785cb5c}
  - picoCTF{947b91a983c93217304f8e5b112e93eaf619e6a9386ab93be93a9b67e53b2fda}
  - picoCTF{a3ed2f602322f749f4cb016515e25b67749efd08ac2f2c53023596cbf0dcbd0f}
  - picoCTF{8e625859eb325d2a69934e4a44c93fcc132e813efb3fdaaa5143147678e9cbf9}
  - picoCTF{8d43c4889ee5b507d1785adfa2592f2fb3d7cf20ebf37ce46595edc46fba3f6d}
  - picoCTF{0020d021e9e38dbb5a5fa432175089d8b76e4a900618c95f8cae14fedaa45b63}
  - picoCTF{69e96b10f560a6a0656a6d950e73e41bcf4226c424bb5622839dda0c66755b14}
  - picoCTF{34c6ca47d858ab18aa2008f4ac31c31570c46186939e6b46458b19082122d4bd}
  - picoCTF{ebfcebe696b1fdbba2abb3b003165152456bd83b6ddfbf180ca366de0dec1b0c}
  - picoCTF{aa125aaeb4723f69dceaa90125a8099a6f3fe0259e068fd82dcbeb76131448bb}
  - picoCTF{80d65857d8d81a92769e8cd136376522d113c4298b331318ce7adcbf5e70104d}
  - picoCTF{00ae773ce4a4b3cf3287f072c13ec7139a74207de635de9d115087bc4f312bae}
  - picoCTF{7e808778b7250893922a17d53f10365b009a7624935850ac5c8140461e49d579}
  - picoCTF{33e80d6e9f56c1f7705c73566d347ccb32b4662171f224b6dfcb6c8fce4f1601}
  - picoCTF{5d921ffbe2709ba82d09603a095530aedae41ab96fd052140cbc64319b7ab0ac}
  - picoCTF{977b385d5dd6abde9cb89ee940b5cfb7179d73d989c6993346d278bff003c154}
  - picoCTF{ca7d3b029817de8f318d8fa521ad1b569f4e8a37358373193522cc7f5628ed49}
  - picoCTF{a820680ab6444b1daf5281192f337aefb4aa95a313c9f270804ef7826ecc298c}
  - picoCTF{998d01dadf1b44eb4ec7b7e8fa11f11bcd2d7d86f3f9e4966dde22d4a84ca113}
  - picoCTF{cb8fe3ec65f890e2f0570c98c4edd3fe4115bc059ac2afb39300c7b66f2302c4}
  - picoCTF{bc2af8cbe0ae0befdd28b14412295243354cd3c7cc74e88d8facb2fd5e6ef34d}
  - picoCTF{09082a0313e16fc36f8076ff86e54e83048a8568f5c2294fea5fb3bcd212e7f2}
  - picoCTF{2386746aeb258914349dc81a85cb5de72e47930c7f11759b4ad9f864efa7b5aa}
  - picoCTF{173306d7b886423d9f79d3d0d05209807ae7b83c445931319830e4e0ad2d2f09}
  - picoCTF{6cb98e2295bbe1f15fd8b8b5908de360d386b98a0ce7e0407e001b453b05be22}
  - picoCTF{132e643c8fdadb54c366072cb33940411fcfd355209fc1ce9b2022ad1cd1b060}
  - picoCTF{044ffca72f0f191b0715ff1a9bff182c810cb2786370cbf8cdc1943c2e7aedf6}
  - picoCTF{b278104c2602442e3db401749c30527d80ba560f9a02c939cb4ff6ea189a140d}
  - picoCTF{7282e048d6d32383b65f3a03b1101219ac73f7f538446b78d1b2b334e0985447}
  - picoCTF{98406c4acbf0f57b3ccbc923aab5a603d70f86d507f422d9bd8656398f53433e}
  - picoCTF{3fe0b2788f30d9cb9f77d3b2752f13c554fe7f0e7a2883e57c8a44b34f35675c}
- Then I read the first hint and understood that all my above things are wrong. Since none of those are flags.
- Again I looked at all the red highlighted things found the one with the base64 encoded text. Did not find the flag.
- Googled the problem. Found [this](https://github.com/Dvd848/CTFs/blob/master/2021_picoCTF/Wireshark_twoo_twooo_two_twoo.md) writeup. This person also found all those flags we found and none worked.
- He also found the base64 encoded string which was flag for him but for me it is not converting into the string.
- Watched this [video](https://www.google.com/search?q=Wireshark+twoo+twooo+two+twoo...&rlz=1C1ONGR_enIN985IN985&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:0dd079bc,vid:mQB_yoAY0gg). He solved the problem with the cmd and I did not understand much.
- Watched this [video](https://www.youtube.com/watch?v=jDY6nW4yNBM). In the video we narrow the things down to the dns query made to destination 18.217.1.57. 
- In the video what we are told is that the data is being sent throught the dns queries little by little in base64 encoded form. And this might be really our flag.
- The text is at the front of .redherring.com
- The base64 encoded text is cGljb0NU RntkbnNf M3hmMWxf ZnR3X2Rl YWRiZWVm fQ==
- I took all those chunks and took to online base64 decoder. Got a flag.
- flag: picoCTF{dns_3xf1l_ftw_deadbeef}
</details>

<details>
<summary>Who are you?</summary>

### Who are you?
- Opened the website. Found no buttons to interact.
- A gif load with text wait a minute who are you? 
- There is script in the source with click event listener on element with class close. On click it will select myAlert element and alert close. But there is no button to click on page.
- Looked at the hint: It ain't much, but it's an RFC https://tools.ietf.org/html/rfc2616
- This is a document on HTTP/1
- Looked in the cookie section nothing found.
- Googled the challenge. Watched [this](https://www.youtube.com/watch?v=su1XD3x5k_E) and [this](https://www.youtube.com/watch?v=lldA9BDjZyw) video.
- Did not understand anything form the 1st video.
- Second video told RFC stands for Request for comments.
- Read [this](https://ctftime.org/writeup/26905) write up. And followed it with the various links it has.
- The site mentions it allows only pico browsers user. So we need to use the header user-agent with value PicoBrowser. User-agent header tells the server the application name of the user in this case PicoBrowser. command used here: **wget --user-agent="PicoBrowser" http://mercury.picoctf.net:39114/**
- We get a index.html file on cat it we see I don't trust users from another site. [Writeup](https://ctftime.org/writeup/26905) suggest us to use referer header here. Referer header contains the partial or full url of the site from which the resource has been requested. This tell the server that where the resource is being used. command here used: **wget --user-agent='PicoBrowser' --referer='http://mercury.picoctf.net:39114/' http://mercury.picoctf.net:39114/**
- We get another index.html. On cat it we see Sorry this site only worked in 2018. [Writeup](https://ctftime.org/writeup/26905) suggest us to use Date header here. Date and time header tells the server at which date and time the request was originated. So here we need to set some date in the year 2018. command used here: **wget --user-agent='PicoBrowser' --referer='http://mercury.picoctf.net:39114/' http://mercury.picoctf.net:39114/ --header='Date: 2018'**
- We get another index.html which says that I don't trust users which can be tracked. [Writeup](https://ctftime.org/writeup/26905) suggest us to use DNT header here. It tells the server that user prefers not to be tracked. command used here is: **wget --user-agent='PicoBrowser' --referer='http://mercury.picoctf.net:39114/' http://mercury.picoctf.net:39114/ --header='Date: 2018' --header='DNT: dnt'**
- We get another index.html which say this site is only for people form sweden. [Writeup](https://ctftime.org/writeup/26905) suggest us to use X-Forwarded-For header here. When user requests something directly form the server the user IP address is written in server logs. But if there are proxies in connection then the ip address of the final proxy is passed to the server which of no use for the server. So to pass a more useful IP address of the client X-forwarded-for header is used. [Writeup](https://ctftime.org/writeup/26905) also suggests us to find a swedish IP address. I used this 31.3.152.55. Command used here is: **wget --user-agent='PicoBrowser' --referer='http://mercury.picoctf.net:39114/' http://mercury.picoctf.net:39114/ --header='Date: 2018' --header='DNT: dnt' --header="X-Forwarded-For: 31.3.152.55"**
- We get anohter index.html file which says that we are from sweden but don't speak swedish. [Writeup](https://ctftime.org/writeup/26905) suggest us to use Accept-language header here. This header tells the server about the local language that the user prefers. The value of this header is set by browser depending on the language of the user-interface. Command user here: **wget --user-agent='PicoBrowser' --referer='http://mercury.picoctf.net: http://mercury.picoctf.net:39114/ --header='Date: 2018' --header='DNT: dnt' --header="X-Forwarded-For: 31.3.152.55" --header="Accept-language: sv"**
- We get another index.html which has the flag.
- flag: picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_20ace0e4}
</details>

<details>
<summary>login</summary>

### login
- Description: My dog-sitter's brother made this website but I can't get in; can you help?
- Open the website and open the cookies in the developer tools thing.
- Type in random username and password. Nothing happening to the cookies.
- Open the source. Find the Script in the index.js.
- Script is asynchronous. Don't Know what is happening to the promise. It waits for the window to load then selects the form element and adds a submit eventListener to it and  prevents the default behaivour of the submit button. creates a r variable to store some values to select the input fields in the form and get their values.
- After getting the values from the input fields it base64 encodes them and then removes the padding = with nothing.
- So the in base64 encoded with some padding at end which is been replaced username: "YWRtaW4" password: "cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ"
- Further in the script we see that our flag is base64 decoded form of the password. But we cannot directly decode the thing since there might be some padding which has been replace with a empty string and will get error if try to do it.
- I created this small python [program](/solution/login.py) run it and then input the password [here] and you will get the flag.
- flag: picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}
</details>

<details>
<summary>advanced-potion-making</summary>

### advanced-potion-making
- Downloaded the file. I had no extension.
- Opened the file in [online hex editor](https://hexed.it/). Saw the IHDR word in the hex editor googled it found [PNG Wikipedia page](https://en.wikipedia.org/wiki/PNG).
- This might be some kind of PNG file which is changed in some way. I have now idea of how to figure it out. There are no hints also.
- Looked at the initial few hex digits they were different from what was shown in the wikipedia file format.
- It might be that the initial bits are changed as they were also changed in one of the previous challenges.
- I also noticed in the hex editor is that there is a lot of XT kind of symbols in the beginning and similarly L2U kind of symbols at the end of the file. My guess is that the file has been padded with some kind of data.
- Googled the problem.
- Found this [writeup](https://www.ctfwriteup.com/picoctf/picomini-by-redpwn/forensics) which had changed the bits. I also did the same using the wikipedia page.
- Opened the file in the paint. I was all red colour and no flag was there.
- The next step in the ctf write up is to use stegsolve to find the flag.
- Watched this [video](https://www.youtube.com/watch?app=desktop&v=MJK6rvOSPPE)
- I was not able to understand any of their solution with all the color change and the stegsolve things.
- So I wrote my own [solution](/solution/advanced_potion_making.py) and provided the explanation. 
### Program Description
- **Objective**
    - We know that the flag is hidden in the image. 
    - But the pixel value of the flag is very similar to the background color. 
    - So what we have to do is to make the difference between the flag pixel value and the background color very large. 
    - It is like flag is written on a 'white paper' with 'almost white ink'. 
    - So we have to do is to make the 'white paper' black and 'almost white ink' completely white. 
    - We cannot do this with naked eye but a computer can do this since it works with pixel value.
- **My Approach**
    - What I did is that I first is to run to through all the individual pixel of the image and store the pixel value of the unique pixel with number of times they occured in the image.
    - Then run through the individual pixel of the image again and find the percentage of this pixel value present in the image using the our previous recorded value of the number of times the various pixel occured in the image.
    - If the percentage of the current pixel is more than 50% then this is a background pixel and we store a black pixel in the new image at the same position
    - If the precentage of the current pixel is less than 50% we store a white pixel at the same position in the new image.
    - After doing the above we store the new image on the disk.
- **Instructions**
    - To run my [solution](/solution/advanced_potion_making.py) you will have to make few setups.
    - You need to have pip installed in the computer. You can find more about it [here](https://pypi.org/project/pip/).
    - Using pip install the pillow module. You can find the instructions to do so [here](https://pillow.readthedocs.io/en/latest/installation.html).
    - Now you have to do is take the uncorrupted copy of the image in a folder.
    - Name the folder to "solution" else change path in the program.
    - Name the image as 'image.png'
    - Then run the program.
    - You will get a new image with name ["image_with_flag.png"](/flag_images/image_with_flag.png).
    - **Sorry** if this solution does not work for you.
- flag: picoCTF{w1z4rdry}
</details>

<details>
<summary>spelling-quiz</summary>

### spelling-quiz
- Downloaded the file to my system.
- Unzip to find 3 files encrypt.py, flag.txt, study-guide.txt
- Opened the encrypt.py.
- Seeing the various things in program we try to run the program in piece form and try to understand what it is doing.
- On looking at the first files variables I googled what does a for loop inside a list do and found this [stackoverflow post](https://stackoverflow.com/questions/11479392/what-does-a-for-loop-within-a-list-do-in-python). This post has examples which explains very nicely what the for loops do.
- os.walk(path) is a method which take a path as argument and then loops through all the file and subfolders in that path and all the files and folder in the subfolder. It basically travels all of the directory tree.
- You can find a very good explanation of os.walk() in the book **Automate the boring stuff with python** chapter 10.
- In the program encrypt.py the loops in files list are going through all the files of the current directory and checking the specific file is a .txt file if so then they are storing the realtive path of that file in the files list.
- In next line we are storing english alphabets as list in variable alphabet.
- We are then shuffling the alphabet list and stroing the shuffled list in the variable shuffled using **[walrus operator](https://medium.com/mlearning-ai/when-and-why-to-use-over-in-python-b91168875453#:~:text=The%20walrus%20operator%20is%20denoted,the%20processing%20of%20large%20data.)**. 
- It then creates a dictionary form alphabet and shuffled list.
- It then loops through all the .txt file in the list files
- Reads all the text in each file and then replaces all the characters using the key value pairs in the dictionary and then writes it back into the original file. Like for key 'a' in dictionary the value may be 'm' depending on the shuffle then the after encryption all the a in the text file will be replaced by m. 
- The character in the file is not present in the text it is kept as it is.
- The value which is stored in variable encrypted is written in a fancy way. I have written it's simplified form below.

```
    encrypted_list = [];
    for c in text:
        if c in dictionary:
            encrypted_list.append(dictionary[c])
        else:
            encrypted_list.append(c);
    encrypted = "".join(encrypted_list);
```

- The value stored in the variable encrypted is then written in the file.
- So now I understand how the things are getting encrypted it is time to get the flag.
- File flag.txt has our flag in the encrypted form.
- study-guides.txt has bunch of string which are encrypted.
- I was looking at the strings and saw this string "bwttxnlrv" which looks quite similar to the butterfly as length is same.
- The above problem is very difficult since every time shuffle is going to generate new dictionary.
- I looked at this [writeup](https://github.com/jon-brandy/CTF-WRITE-UP/blob/5b947ed4ee2de28aa10675fa1ec5c11fe4ed8d48/Asset/spelling-quiz/README.md)
- It suggested to use [this](https://github.com/jon-brandy/CTF-WRITE-UP/blob/5b947ed4ee2de28aa10675fa1ec5c11fe4ed8d48/Asset/spelling-quiz/README.md) online tool to solve the problem and also gave instructions of how to use it in the writeup.
- It give text on solving perhaps the dog jumped over was just tired.
- We just have to replac space with _ and put it in picoCTF{}
- flag: picoCTF{perhaps_the_dog_jumped_over_was_just_tired}

</details>

<details>
<summary>Glitch cat</summary>

### Glitch Cat
- Looking from the title we can see the thing might be related to the command cat.
- On running the net cat command we get this text 'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'.
- Guessing from the text we can see that there is some string and the bits with chr.
- The text in the brackets might be hexadecimal. And we can then convert the hexadecimal to the int values which might be the ASCII value that might be our flag.
- Created [this](./solution/glitch_cat.py) program to convert the hex value to string char. Replace the chr thing with the string values from the program.
- flag: picoCTF{gl17ch_m3_n07_9c42a45d}
</details>

<details>
<summary>convertme.py</summary>

### convertme.py
- Question mentions to convert the given number from decimal to binary to flag.
- Run the python script it asked to me to convert 92 from decimal base to binary. Entered 1011100 which is 92 in binary. Got the flag.
- flag: picoCTF{4ll_y0ur_b4535_722f6b39}
</details>

<details>
<summary>fixme1.py</summary>

### fixme1.py
- Question mentions to find the syntax error in python program to print the flag.
- To do this we can run the python script and then the computer will tell us where the error and we can then go from there.
- The syntax error is in line 20 and the error is unexpected indent.
- Print statement was indented. Removed the indent. Ran the script again.
- Got the flag.
- flag: picoCTF{1nd3nt1ty_cr1515_182342f7}
</details>


<details>
<summary>Codebook</summary>

### Codebook
- Dowloaded the two files and ran the code got the flag. I don't understand why this problem is so simple.
- flag: picoCTF{c0d3b00k_455157_7d102d7a}
#### Program Description
- But my brain was not quiet and guilt tripping me that this is not the way to do things and we need to really know what is happening in the thing.
- So we are here. I opened the file in the editor.
- There is main function which call the print_flag function which is opening the file codebook.txt. So I directly pasted the text form the codebook.txt file in the varible codebook and removed the import and the try blocks and ran the program to see if it still works and it does.
- It is then taking the character at specific index and then storing in the variable in the password. Printed the password and this was what is storing ```chthonian```.
- This call the str_xor function with encoded flag and password as the argument.
- We move the str_xor function. There the key that is password in stored in a varibale name new_key.
- Then we run a while loop to make the new_key variable lenght same as the length of the encoded flag which is stored in the variable named secret.
- We increase the length of the new_key by adding the characters of the key to the back using variable i and making sure it does not go above the length of the the key by modding it.
- In the return statement we are doing is XOR operation on the ASCII value of the characters of the two word stored in variable secret and new_key respectively and at same index.
- ```
    secret = "_^☻>ZV]E]X1^♣_SZ►_♫‼"
    new_key = "chthonianchthonianchthonianchthon"
    dict_secret_key = zip(secret, new_key) # creates a dictionary with characters of secret as key and of new_key as values
    flag = []
    for (secret_c, new_key_c) in dict_secret_key:
        charc = chr(ord(secret_c) ^ ord(new_key_c)) # XOR operation on the ASCII values
        flag.append(charc) # storing each flag character in the list flag
    print("".join(flag)) # joining the flag to form a string.
    ```
- The most important thing here is that though by couting the characters in the secret and the new_key we can see the characters in the new_key are more than in the secret. So I don't understand why the while loop entered so many characters in the new_key.
- I think this may be something to do with the bytes used to store the ASCII values of the characters.
- Like if we run ```ord('☻')``` we get a number 9787 which cannot stored in single byte. So we need more bytes so the length of the string secret is 33 though it has less characters in it.
</details>

<details>
<summary>PW Crack 2</summary>

## Descritption
- Wget the python file and the flag into the webshell
- Open the python program in the nano.
- We see that the password is being compared to some hexadecimal string.
- So we can print those string to get the password.
- ``` print(chr(int('0x33', 16)),chr(int('0x39', 16)),chr(int('0x63', 16)),chr(int('0x65', 16))) ```
- Enter the above command before the program ask for the pasword and replace the hex characters with the one in the if conditions. Save the file and then run the program.
- You will then have to enter the printed string as passowrd and make sure to remove the space since the comma in print statement add space.
- You will then get the flag.
- flag: picoCTF{tr45h_51ng1ng_502ec42e}

</details>


<details>
<summary>PW Crack 3</summary>

## Descritption
Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too.
There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

## Steps
- On wget the file in the webshell open the python file and then I tried to print the correct_pw_hash.
- It was a hex string and did not understand much from it.
- So then I tough of generating the md5 hash of all the possible given passwords.
- I just used a for loop to do and called the level_3_pw_check function after the loop.
- ```
    pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]

    for i in pos_pw_list:
            print(hash_pw(i), i)

    level_3_pw_check()
  ```
- The above loop printed all the password and their hashes and looking at the correct password hash printed I got the correct password.
- flag: picoCTF{m45h_fl1ng1ng_2b072a90}


</details>

<details>
<summary>PW Crack 4</summary>

## Descritption
Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too.
There are 100 potential passwords with only 1 being correct. You can find these by examining the password checker script.

## Steps
- Wget all the files in the webshell
- Then open the python file in nano.
- Change the function definition of level_4_pw_check to ``` def level_4_pw_check(hash_pass):```
- Instead of taking the input from user store the function parameter hash_pass in the user_pw variable.
- Now remove the call to the level_4_pw_check function.
- Under the list pos_pw_list make a for loop and iterate over all the elements of the pos_pw_list and call the function level_4_pw_check and pass the element as function parameter in this function call and you will get the flag.
- In this for loop we are entering all the passwords instead of taking any input from the user.
- flag: picoCTF{fl45h_5pr1ng1ng_ae0fb77c} 
</details>

<details>
<summary>PW Crack 5</summary>

## Descritption
Can you crack the password to get the flag?
Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. Here's a dictionary with all possible passwords based on the password conventions we've seen so far.

## Steps
- Wget all the files in the webshell
- Then open the python file in nano.
- Change the function definition of level_5_pw_check to ``` def level_5_pw_check(hash_pass):```
- Instead of taking the input from user store the function parameter hash_pass in the user_pw variable.
- Now remove the call to the level_4_pw_check function.
- Now read all the lines of the dictionary file into the a variable as list and iterate over the elements of the entire list. Call the function level_5_pw_check and pass the first four characters of the element as function parameter in this function call and you will get the flag.
- In this for loop we are entering all the passwords instead of taking any input from the user.
- flag: picoCTF{h45h_sl1ng1ng_36e992a6} 
</details>

<details>
<summary>Serpentine</summary>

## Descritption
Find the flag in the Python script!
Download Python script

## Steps
- Downloaded the python file on my machine and opened it in vscode.
- On looking at the file we can see we have to enter the options values to get the flag but when we enter option b the print_flag function call is missing so we can add that function call in the elif condition for b and then run the file to see what happens.
- Doing so we get the flag. Though the python program is doing other things too but I did not care to look into it so sorry.
- flag: picoCTF{7h3_r04d_l355_7r4v3l3d_ae0b80bd}
</details>

<details>
<summary>basic-mod1</summary>

## Descritption
We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message here.
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Steps
- I downloaded the message file on my machine.
- Then I wrote the python script to do what they told in the description.
- This is the python [program](./solution/basic_mod1.py). You can run the program and then copy and paste the message text and then it will give the flag.
- flag: picoCTF{R0UND_N_R0UND_ADD17EC2}
</details>

<details>
<summary>basic-mod2</summary>

## Descritption
A new modular challenge!
Download the message here.
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Steps
- I downloaded the message file on my machine.
- You can read more about the modular inverse of number on [Khan Acadmey Modular Inverse](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-inverses).
- I wrote the python script to do what they told in the description using the naive method from the **Khan Acadmey** article.
- This is the python [program](./solution/basic_mod2.py). You can run the program and then copy and paste the message text and then it will give the flag.
- The problem is that that the Khan acadmey article said it was a naive method so I googled how to find the modular inverse and found this [video](https://www.youtube.com/watch?v=KqoIlojTrmw) which is the solution to this challenge. It helped to see if I was doing something wrong. 
- In video they used the pow function to find the modular inverse. So got a better way.
- flag: flag: picoCTF{1NV3R53LY_H4RD_DADAACAA}
</details>

<details>
<summary>credstuff</summary>

## Descritption
We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it?
Download the leak here.
The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.

## Steps
- Download the file and then extract the file.
- I wrote [this python program](/solution/credstuff.py) which reads the passwords and the usernames txt file and the create a dictionary and the find the passwords of the username "cultiris" and prints it.
- The passwords looks some kind of the ceaser cipher. Copy that password and use [this ceaser cipher](/solution/trivial_Flag_transfer.py) program to get all the ceaser cipher with all the 26 keys.
- Run the program and paste the password as input and you will get 26 deciphered text one is going to be the flag with picoCTF{...}.
- flag: picoCTF{C7r1F_54V35_71M3}

</details>

<details>
<summary>Enhance!</summary>

## Descritption
Download this image file and find the flag.
Download image file

## Steps
- Dowloaded the svg file opened it saw a concentric black and white circle.
- Opened the svg in browse and inspected it.
- Expanded the text element there was flag in the tspan elements.
- flag: picoCTF{3nh4nc3d_aab729dd}
</details>

<details>
<summary>file-run1</summary>

## Descritption
A program has been provided to you, what happens if you try to run it on the command line?
Download the program here.

## Steps
- Wget the file in the webshell.
- I tried running the file using ./run but got the error of permission denied.
- Since in problem it is written we have to run the file using the command line so I tried to make it a executable that I learned in the course [missing semester of CS](https://missing.csail.mit.edu/).
- To make a file executable we have to run the command ```chmod +x filename```.
- Then I ran the file with just typing the name of the file in the terminal.
- It printed out the flag.
- flag: picoCTF{U51N6_Y0Ur_F1r57_F113_9bc52b6b}
</details>

<details>
<summary>file-run2</summary>

## Descritption
Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?
Download the program here.

## Steps
- Wget the file in the webshell.
- Try to run the file with the ./filename got permission denied.
- Do the chmod thing to make the file executable with ```chmod +x filename```.
- Then again run the file. Got error run file with the text thing.
- Problem tells us to run the file with the input text.
- Tried to pipe the text into the run nothing happened.
- Then googled how to run a executable with the text as input. Got answer ```./filename text```
- Did this and got the flag.
- flag: picoCTF{F1r57_4rgum3n7_96f2195f}
</details>

<details>
<summary>template</summary>

## Descritption

## Steps

</details>
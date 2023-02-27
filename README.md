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
<summary>Template</summary>

### Things to add
- content
</details>



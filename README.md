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
<summary>Template</summary>

### Things to add
- content
</details>



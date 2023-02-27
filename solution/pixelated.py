# INSTRUCTIONS
# make sure that both the images from the problem are in same directory as the program
# make sure you have installed the pillow module. For instruction google pillow module in python.
# to install the pillow module you must have pip installed. For more instruction google how to install pip on your os.
# after doing all the above do this.

from PIL import Image;

scrambled_1 = Image.open('solution\scrambled1.png');
scrambled_2 = Image.open('solution\scrambled2.png');

width, height = scrambled_1.size;

decipher_image = Image.new('RGB', (width, height));

for x in range(width):
    for y in range(height):
        r1, g1, b1 = scrambled_1.getpixel((x, y));
        r2, g2, b2 = scrambled_2.getpixel((x, y));
        decipher_image.putpixel((x,y), ((r1+r2)%256, (g1+g2)%256, (b1+b2)%256));

decipher_image.save('solution\decipherImage.png');

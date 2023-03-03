# INSTRUCTIONS
# make sure that the images from the problem are in same directory as the program and change the name of the directory to solution.
# rename the un corrupted image to image.png.
# make sure you have installed the pillow module. For instruction google pillow module in python.
# to install the pillow module you must have pip installed. For more instruction google how to install pip on your os.
# this thing might not work for you so sorry.
# after doing all the above do this.

from PIL import Image;

def findPercentage(num_of_pixels):
    total = width * height;
    return int((num_of_pixels / total) * 100);

# open the image whose hex values have been corrected.
red_original = Image.open('solution\image.png');

# find the width and heigth of the image.
width, height = red_original.size;

# create a new image which has a same height and width as the original un corrupted image.
image_with_flag = Image.new('RGB', (width, height));

unique_rgb_val = [];

# run through all the pixel value of the original image to find all the different pixiel in it which might not be visible to the naked eye.
# all the different pixel value in the image are stored in the list unique_rgb_val with the number of times they are in the image.
for x in range(width):
    for y in range(height):
        r, g, b = red_original.getpixel((x, y));
        rgb_val = [r, g, b];
        if(not rgb_val in unique_rgb_val):
            unique_rgb_val.append(rgb_val);
            unique_rgb_val.append(1);
        else:
            rgb_val_index = unique_rgb_val.index(rgb_val);
            unique_rgb_val[rgb_val_index+1] += 1;

print(unique_rgb_val); #[[238, 18, 29], 2973494, [239, 18, 29], 57791, [238, 17, 28], 4193, [237, 17, 27], 42]

# we run through the original image again and this time we take the single pixel value
# find the number of times it occured in the image to find the percentage of it using unique_rgb_val and the function findPercentage
# if the percentage of the current pixel is more than 50 we put a black pixel in the image_with_flag else a white.
for x in range(width):
    for y in range(height):
        r, g, b = red_original.getpixel((x, y));
        rgb_val = [r, g, b];
        rgb_val_index  = unique_rgb_val.index(rgb_val);
        percentage_of_pixel = findPercentage(unique_rgb_val[rgb_val_index+1]);
        if(percentage_of_pixel > 50):
            image_with_flag.putpixel((x, y), (0, 0, 0));
        else: 
            image_with_flag.putpixel((x, y), (255, 255, 255))

# save the  image.  
image_with_flag.save('solution\image_with_flag.png');
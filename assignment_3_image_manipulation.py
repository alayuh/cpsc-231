# Name (ID): Sophia Chen (30309573) and Aleah Layos (30250766)
# Tutorial: 09
# Sophia Chen did about 50%. Aleah Layos did about 50%.

# import SimpleGraphics
from SimpleGraphics1 import *

## asks user for two image file names and combination option
# @param: (none)
# @return: two image filenames and users combination choice
def handleInput():
    first_image = input("Enter the name of the first image: ")
    second_image = input("Enter the name of the second image: ")
    # displays three image combination options
    print("Combine one of the following options:")
    print("1 - combine two whole images")
    print("2 - blend  horizontally")
    print("3 - blend vertically")
    combination_value = int(input(">> "))

    # repeatedly keep asking until user enters valid option
    while combination_value < 1 or combination_value > 3:
        print("Please enter 1, 2, or 3:")
        print("1 - combine two whole images")
        print("2 - blend horizontally")
        print("3 - blend vertically")
        combination_value = int(input(">> "))

    return first_image, second_image, combination_value

## blend two pixels from different images by averaging their rgb values
# @param image_1: first original image
# @param image_2: second original image
# @param x_pixel: x coordinate of the pixel
# @param y_pixel: y coordinate of the pixel
# @return: the average of red, green, and blue values
def blendPixel(image_1, image_2, x_pixel, y_pixel):
    r1, g1, b1 = getPixel(image_1, x_pixel, y_pixel)
    r2, g2, b2 = getPixel(image_2, x_pixel, y_pixel)

    # calculates average of each rgb value
    red = (r1 + r2) // 2
    green = (g1 + g2) // 2
    blue = (b1 + b2) // 2

    return red, green, blue

## combine two images by blending every pixel
# @param image_1: first original image
# @param image_2: second original image
# @return: a new image with all pixels blended
def combineAll(image_1, image_2):
    width = getWidth(image_1)
    height = getHeight(image_1)
    new_image = createImage(width, height)

    # goes through every pixel and blends colour into new image
    for y in range(height):
        for x in range(width):
            red, green, blue = blendPixel(image_1, image_2, x, y)
            putPixel(new_image, x, y, red, green, blue)

    return new_image

## combine parts of two images with 100 pixel blend
# @param image_1: first original image
# @param image_2: second original image
# @param user_option: 2 for horizontal blend or 3 for vertical blend
# @return: a new image with parts of both images combined
def combineParts(image_1, image_2, user_option):
    image_width = getWidth(image_1)
    image_height = getHeight(image_1)
    combined_image = createImage(image_width, image_height)

    # goes through each pixel to decide which image its colour comes from
    for pixel_y in range(image_height):
        for pixel_x in range(image_width):

            # horizontal blend with a 100-pixel strip in middle
            if user_option == 2:
                middle_height = image_height // 2

                if pixel_y < middle_height - 50:
                    red, green, blue = getPixel(image_1, pixel_x, pixel_y)

                elif pixel_y < middle_height + 50:
                    red, green, blue = blendPixel(image_1, image_2, pixel_x, pixel_y)

                else:
                    red, green, blue = getPixel(image_2, pixel_x, pixel_y)

            # vertical blend with a 100-pixel strip in middle
            else:
                middle_width = image_width // 2

                if pixel_x < middle_width - 50:
                    red, green, blue = getPixel(image_1, pixel_x, pixel_y)

                elif pixel_x < middle_width + 50:
                    red, green, blue = blendPixel(image_1, image_2, pixel_x, pixel_y)

                else:
                    red, green, blue = getPixel(image_2, pixel_x, pixel_y)

            putPixel(combined_image, pixel_x, pixel_y, red, green, blue)

    return combined_image

## runs program by loading, combining and displaying two images
# @param: (none)
# @return: (none)
def main():
    first_image, second_image, combination_value = handleInput()

    # loads two images
    image_1 = loadImage(first_image)
    image_2 = loadImage(second_image)

    # resizes output window to match size of original images
    image_width = getWidth(image_1)
    image_height = getHeight(image_1)

    resize(image_width, image_height)

    # chooses combination method based on user input
    if combination_value == 1:
        combined_image = combineAll(image_1, image_2)
    else:
        combined_image = combineParts(image_1, image_2, combination_value)

    # display the final combined image
    drawImage(combined_image, 0, 0)

# runs the program
main()

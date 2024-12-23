from source import *

with open("source/tests/test_images/panda.bmp", "rb") as f:
    img1_data = f.read()

with open("source/tests/test_images/color.bmp", "rb") as f:
    img2_data = f.read()

for x in range(10, 101, 10):
    print(x)
    img1 = Image(img1_data, size = (x,x//2))
    img2 = Image(img2_data, size = (x,x//2))

    img1.print_image()
    img2.print_image()

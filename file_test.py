from source import *

for x in range(10, 101, 10):
    print(x)
    img1 = Image("source/tests/test_images/panda.bmp", size = (x,x//2))
    img2 = Image("source/tests/test_images/color.bmp", size = (x,x//2))

    img1.print_image()
    img2.print_image()


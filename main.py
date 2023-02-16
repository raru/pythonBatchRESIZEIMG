# from PIL import Image
# foo = Image.open('//Users/raru/Desktop/EricaSalguero/wetransfer_apartamento-brooklin-02_2023-02-14_2023/ES140422-0090.jpg')  # My image is a 200x374 jpeg that is 102kb large
# foo.size  # (200, 374)
#  # downsize the image with an ANTIALIAS filter (gives the highest quality)
# foo = foo.resize((160,300),Image.ANTIALIAS)
# foo.save('//Users/raru/Desktop/EricaSalguero/wetransfer_apartamento-brooklin-02_2023-02-14_2023/ES140422-0090_scaled.jpg', quality=95)  # The saved downsized image size is 24.8kb


#!/usr/bin/python
from PIL import Image
import os, sys

# path
path = "//Users/raru/Desktop/EricaSalguero/apartamento-jardins/"
dirs = os.listdir( path )

resize_ratio = 0.5  # where 0.5 is half size, 2 is double size


def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)

            new_image_height = int(im.size[0] / (1/resize_ratio))
            new_image_length = int(im.size[1] / (1/resize_ratio))

            imResize = im.resize((new_image_height, new_image_length), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()
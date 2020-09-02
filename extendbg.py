from PIL import Image

import os 
def white_bg_square(img):
    "return a white-background-color image having the img in exact center"
    size = (max(img.size),)*2
    layer = Image.new('RGB', size, (255, 255, 255))
    layer.paste(img, tuple(
        map(lambda x: int((x[0]-x[1])/2), zip(size, img.size))))
    return layer


def main():
    # old_im = Image.open('Duplex-Receptacle.png')
    # square_one = white_bg_square(img)
    # square_one.resize((1000, 1000), Image.ANTIALIAS)
    # square_one.save('extendedrecep.png')
    # import Image

    # old_im = Image.open('someimage.jpg')
    for item in sorted(os.listdir("train")):
        print(item)
        old_im = Image.open("train/"+item)
        old_size = old_im.size


        new_size = (122, 129)
        new_im = Image.new("RGB", new_size,(255, 255, 255) )  # luckily, this is already black!
        new_im.paste(old_im, (int((new_size[0]-old_size[0])/2),
                            (int((new_size[1]-old_size[1])/2))))

        new_im.save("train/"+ item)
    # new_im.save('someimage.jpg')


main()
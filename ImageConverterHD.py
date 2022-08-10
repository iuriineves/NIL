from PIL import Image

def createImage(fileDirectory, imgName):
    img = Image.open(fileDirectory)
    img = img.convert('RGB')
    imgtext = ''

    repeater = 1
    lastcolor = ''
    pixels = ''
    screenx, screeny = 320, 222
    imgx, imgy = img.size
    palette = []

    if imgx < imgy:
        img = img.resize((round(imgx * (screeny / imgy)), screeny))
    elif imgx > imgy:
        img = img.resize((screenx, round(imgy * (screenx / imgx))))
    else:
        img = img.resize((screeny, screeny))

    img = img.convert('P', palette=Image.Palette.ADAPTIVE, colors=64)
    img = img.convert('RGB')
    imgx, imgy = img.size

    for i in range(len(img.getcolors())):
        palette.append(img.getcolors()[i][1])

    base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz*+!()[]&#=-_'

    for color in list(img.getdata()):
        imgtext += base64[palette.index(color)]

    file = open(f"{imgName}.py", "w", encoding='utf-8')
    file.write(f"""

from kandinsky import color, get_pixel, set_pixel, draw_string, fill_rect

base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz*+!()[]&#=-_'

orientation = ''
pixel = -1

imgx, imgy = {img.size}

palette = {palette}

image = '{imgtext}'

if imgx == 320:
    space = round((222 - imgy) / 2.5)
    orientation = 'h'
elif imgy == 222:
    space = round((360 - imgx) / 2.5)
    orientation = 'v'
    

xstartpoint = 0
ystartpoint = 0
if orientation == 'v':
    xstartpoint = space
elif orientation == 'h':
    ystartpoint = space

fill_rect(0, 0, 320, 222, (35, 39, 42))
for k in range(ystartpoint, (imgy) + ystartpoint):
    for i in range(xstartpoint, (imgx) + xstartpoint):
        pixel = pixel + 1
        set_pixel(i, k, palette[base64.index(image[pixel])])

    """)
    file.close()

imgdir = input('Image Directory: ')
filenm = input('File Name: ')

createImage(imgdir, filenm)
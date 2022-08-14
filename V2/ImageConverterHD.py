from PIL import Image

def createImage(fileDirectory, imgName):
    img = Image.open(fileDirectory)
    img = img.convert('RGB')
    imgtext = ''
    i = 0

    repeater = 1
    lastcolor = ''
    pixels = ''
    screenx, screeny = 320, 222
    imgx, imgy = img.size
    palette = []

    img = img.resize((screenx, round(imgy * (screenx / imgx))))
    if img.size[1] > screeny:
        img = img.resize((round(imgx * (screeny / imgy)), screeny))

    img = img.convert('P', palette=Image.Palette.ADAPTIVE, colors=64)
    img = img.convert('RGB')
    imgx, imgy = img.size

    for k in range(len(img.getcolors())):
        palette.append(img.getcolors()[k][1])

    base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz*+!()[]&#=-_'

    for color in list(img.getdata()):
        i += 1
        #print(i)
        #print(len(img.getdata()))
        if color == lastcolor:
            repeater += 1
        elif color != lastcolor:
            if repeater > 1:
                imgtext += str(repeater)
            repeater = 1
            imgtext += base64[palette.index(color)]
        lastcolor = color
        
        if i == len(img.getdata()):
            imgtext += str(repeater)

    file = open(f"{imgName}.py", "w", encoding='utf-8')
    file.write(f"""



from kandinsky import color, get_pixel, set_pixel, draw_string, fill_rect

base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz*+!()[]&#=-_'
nums = '0123456789'

orientation = ''
pixel = 0
imgpixel = 0
repeater = ''
repeated = 0

imgx, imgy = {img.size}

palette = {palette}

image = '{imgtext}'

if imgx == 320:
    space = round((222 - imgy) / 2)
    orientation = 'h'
elif imgy == 222:
    space = round((320 - imgx) / 2)
    orientation = 'v'
    

xstartpoint = 0
ystartpoint = 0
if orientation == 'v':
    xstartpoint = space
elif orientation == 'h':
    ystartpoint = space

def pixelsToCoord(pixels):
    y, x = 0, 0

    while pixels > imgx - 1:
        y += 1
        pixels -= imgx
    x = pixels
    return x, y

fill_rect(0, 0, 320, 222, (35, 39, 42))

while imgpixel < imgx * imgy:
    if image[pixel] in base64:
        color = image[pixel]
        if pixel + 1 <= len(image) and image[pixel+1] in nums:
            while True:

                if pixel + 1 < len(image) and image[pixel+1] in nums:
                    repeater += image[pixel+1]
                    pixel += 1
                else:
                    repeated = int(repeater.strip())
                    repeater = ''
                    while repeated > 0:
                        x, y = pixelsToCoord(imgpixel)
                        set_pixel(xstartpoint + x, ystartpoint + y, palette[base64.index(color)])
                        imgpixel += 1
                        repeated -= 1
                        i = 0
                    pixel += 1
                    break
        else:
            x, y = pixelsToCoord(imgpixel)
            set_pixel(xstartpoint + x, ystartpoint + y, palette[base64.index(color)])
            imgpixel += 1
            pixel += 1
    """)
    file.close()

imgdir = input('Image Directory: ')
filenm = input('File Name: ')

createImage(imgdir, filenm)
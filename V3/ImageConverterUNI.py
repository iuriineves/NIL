from PIL import Image
import colorama

def createImage(fileDirectory, imgName, res):
    img = Image.open(fileDirectory)
    img = img.convert('RGB')
    imgtext = ''
    i = 0

    res = int(res)
    quality = ''
    repeater = 1
    lastcolor = ''
    screenx, screeny = round(320 / res), round(222 / res)
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

    if res == 1:
        cmd = 'set_pixel(xstartpoint + x, ystartpoint + y, palette[base64.index(color)])'
        quality = 'HD'
    elif res >= 2:
        cmd = f'fill_rect(xstartpoint + x * {res}, ystartpoint + y * {res}, {res}, {res}, palette[base64.index(color)])'
        quality = 'SD'

    file = open(f"{imgName}{quality}.py", "w", encoding='utf-8')
    file.write(f"""



from kandinsky import set_pixel, fill_rect

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

if imgx == {round(320 / res)}:
    space = round((222 - imgy * {res}) / 2)
    orientation = 'h'
elif imgy == {round(222 / res)}:
    space = round((320 - imgx * {res}) / 2)
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
                        {cmd}
                        imgpixel += 1
                        repeated -= 1
                        i = 0
                    pixel += 1
                    break
        else:
            x, y = pixelsToCoord(imgpixel)
            {cmd}
            imgpixel += 1
            pixel += 1
    """)
    file.close()

imgdir = input('Image Directory: ')
filenm = input('File Name: ')
res = input('Image Resolution ("1" - HD | "2" - SD | >2 - LD and smaller): ')

createImage(imgdir, filenm, res)

print(f"Image '{filenm}' converted.")
if res == '1':
    print("WARNING - The image resolution was set to HD, so there's a high chance that the calculator won't be able to load the image. Only use the HD version if the image requires readability or has flat colors.")
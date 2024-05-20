from PIL import Image, ImageDraw, ImageColor
import os.path

def img_convert_n_draw(frmt1, frmt2):
    root = 'test_zip'
    for i in os.listdir(root):
        n_part = i.split('.')
        path = os.path.join(root, n_part[0])
        if not os.path.exists(path) and n_part[1] == frmt1:
            im_path = os.path.join(root, i)
            im = Image.open(im_path)
            im_n = os.path.join(root, (str(n_part[0]) + '.' + frmt2))
            if not os.path.isfile(im_n):
                im = im.resize((1000, 1000))
                rect = ImageDraw.Draw(im)
                rect.rectangle([200, 200, 800, 800], outline='black')
                text = 'Hello, \n World!'
                rect.multiline_text((500, 500), text, font_size=80, anchor='mm', fill='black', align='center')
                im.save(im_n)
            else:
                print('Файл уже существует')

img_convert_n_draw('png', 'bmp')

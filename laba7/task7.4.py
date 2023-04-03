from PIL import Image

images = [Image.open('C:/Users/user/Desktop/laba7/1.jpg'), Image.open('C:/Users/user/Desktop/laba7/2.jpg'),
          Image.open('C:/Users/user/Desktop/laba7/3.jpg'), Image.open('C:/Users/user/Desktop/laba7/4.jpg'),
          Image.open('C:/Users/user/Desktop/laba7/5.jpg')]
water_mark = Image.open('C:/Users/user/Desktop/laba7/watermark.png')
water_mark = water_mark.resize((200, 200))

for i, img in enumerate(images):
    img = img.convert('RGBA')
    fg_img_trans = Image.new("RGBA", img.size)
    fg_img_trans.paste(water_mark, (0, 0))
    transparent_image = Image.new('RGBA', img.size)
    fg_img_trans = Image.blend(fg_img_trans, transparent_image, 0.5)
    img.paste(fg_img_trans, (0,0), fg_img_trans)
    #img.paste(blended, (0, 0))
    new = f'imgready_{i + 1}.png'
    print(new)

    img.save(f'C:/Users/user/Desktop/laba7/task4/{new}')

# f'{}' - форматная строка

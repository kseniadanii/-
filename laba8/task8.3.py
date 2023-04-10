from PIL import Image, ImageDraw, ImageFont

user_text = input("Введите имя для поздравления ")
img = Image.open("C:/Users/user/Desktop/laba8/Поздравление.jpg")
draw = ImageDraw.Draw(img)
font1 = ImageFont.truetype("times", 95)
font2 = ImageFont.truetype("impact", 100)
new = f'{user_text},'
draw.text((245, 470), new, (219, 86, 134), font=font1, stroke_width=3, stroke_fill=(219, 86, 134))
draw.text((245, 600),'Поздравляю!', '#abed8d', font=font2, stroke_width=1, stroke_fill='#609149')
img.show()
img.save('C:/Users/user/Desktop/laba8/Готовое_поздравление.png')

from PIL import Image

image = Image.open('C:/Users/user/Desktop/laba7/meow.jpg')

res_image = image.reduce(3)
res_image.save('C:/Users/user/Desktop/laba7/meow2.png')

res_image2 = res_image.transpose(Image.FLIP_LEFT_RIGHT)
res_image2.save('C:/Users/user/Desktop/laba7/meowleftright.png')

res_image3 = res_image.transpose(Image.FLIP_TOP_BOTTOM)
res_image3.save('C:/Users/user/Desktop/laba7/meowuodown.png')


from PIL import Image

image = Image.open('C:/Users/user/Desktop/laba7/meow.jpg')
image.show()
print(image.size)
print(image.format)
print(image.mode)

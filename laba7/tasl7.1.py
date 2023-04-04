from PIL import Image

image = Image.open('C:/Users/user/Desktop/laba7/meow.jpg')
image.show()
print("Размер:", image.size)
print("Формат:", image.format)
print("Цветовая модель:", image.mode)

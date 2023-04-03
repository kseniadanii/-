from PIL import Image, ImageFilter

images = [Image.open('C:/Users/user/Desktop/laba7/1.jpg'), Image.open('C:/Users/user/Desktop/laba7/2.jpg'),
          Image.open('C:/Users/user/Desktop/laba7/3.jpg'), Image.open('C:/Users/user/Desktop/laba7/4.jpg'),
          Image.open('C:/Users/user/Desktop/laba7/5.jpg')]

for i, img in enumerate(images):
    img = img.filter(ImageFilter.CONTOUR)
    new = f'imgready_{i + 1}.png'
    print(new)
    img.save(f'C:/Users/user/Desktop/laba7/ready/{new}')



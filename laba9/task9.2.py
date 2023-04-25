import os

from PIL import Image, ImageFilter

folder_input = 'C:/Users/user/PycharmProjects/Algorit/laba9/input9.1'
folder_output = 'C:/Users/user/PycharmProjects/Algorit/laba9/output9.1'
if not os.path.exists(folder_output):
    os.mkdir(folder_output)
for i in os.listdir(folder_input):
    if i.endswith('.jpg') or i.endswith('.png'):
        full_path = os.path.join(folder_input, i)
        img = Image.open(full_path)
        img = img.filter(ImageFilter.CONTOUR)
        full_path2 = os.path.join(folder_output, i)
        img.save(full_path2)

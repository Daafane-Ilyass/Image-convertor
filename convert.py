import os, sys
from PIL import Image

image_folder = sys.argv[1]
convert_folder = sys.argv[2]
if not os.path.exists(convert_folder):
    os.mkdir(convert_folder)
for folder in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{folder}')
    image_name = os.path.splitext(folder)[0]
    img.save(f'{convert_folder}{image_name}.png','png')
    print(f'{image_name} converted')
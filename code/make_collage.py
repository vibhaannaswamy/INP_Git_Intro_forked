from PIL import Image, ImageDraw, ImageOps, ImageFont
import glob
import os
import random
import numpy as np

def concat_images(image_paths, size, shape=None):
    # Open images and resize them
    width, height = size
    images = map(Image.open, image_paths)
    images = [ImageOps.fit(image, size, Image.ANTIALIAS) 
              for image in images]
    
    # Create canvas for the final image with total size
    shape = shape if shape else (1, len(images))
    image_size = (width * shape[1], height * shape[0])
    image = Image.new('RGB', image_size)
    myFont = ImageFont.truetype('../code/SourceCodePro-BoldItalic.ttf', 30)
    
    # Paste images into final image
    for row in range(shape[0]):
        for col in range(shape[1]):
            offset = width * col, height * row
            idx = row * shape[1] + col
            if idx < len(image_paths):
                draw = ImageDraw.Draw(images[idx])
                name = image_paths[idx].split("/")[-1][:-5]
                draw.text((0, 0),name,fill=(255,0,0,255) , font=myFont)
                image.paste(images[idx], offset)
    
    return image

# Get list of image paths
folder = '../photos'
ext = [".jpeg", ".jpg"]
image_paths = [os.path.join(folder, f) 
               for f in os.listdir(folder) if f.endswith(tuple(ext))]

collage_size = np.sqrt(len(image_paths))

# Create and save image grid
image = concat_images(image_paths, (300, 300), (int(np.round(collage_size)),int(np.ceil(collage_size))))
image.save('../collage.jpg', 'JPEG')


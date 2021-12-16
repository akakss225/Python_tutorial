import numpy as np
from PIL import Image
import os
input_dir = 'c:/inputImage/'
output_dir = 'c:/outputImage/'
output_npy = 'c:/outputNpy/'
npy=[]
file_list = os.listdir(input_dir)
for png in file_list:
    image = Image.open(input_dir + png).convert('L')
    image.save(output_dir + png)

    pixel = np.array(image)
    # pixel = 255 - pixel
    npy.append(pixel)

np.save(output_npy + "images.npy", np.array(npy))

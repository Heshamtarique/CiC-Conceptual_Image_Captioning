import os
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# loading the image data and storing the name of image in "image/key" column

def load_image(directory, num_images= None):
    try:
        image_data = {'image': [], 'image/key': []}
        
        # is there is no image in the folder...
        if num_images is not None and num_images <=0:
            print("number of images should be greater than 0")
            return None
        
        count= 0
        for file_name in os.listdir(directory):
            if file_name.endswith(('.jpg')):
                # if there is an image file (ending with .jpg)
                file_path = os.path.join(directory, file_name)
                #loading the image we have ---
                image = Image.open(file_path)
                # converting image to numpy array
                image_array = np.array(image)
                
                # storing image array and its filename as we have to later merge 
                # caption file and the image data based on the image/key id.
                image_data['image'].append(image_array)
                image_data['image/key'].append(file_name[:-4])
                count+=1
                if num_images is not None and count>=num_images:
                    break
        df_images = pd.DataFrame(image_data)
        return df_images
    except Exception as e:
        print(f"Error: {e}")
        return None
                    
directory = ".../user/multilingual_image_data"                    
num_images = int(input("how many images??? "))
df_images = load_image(directory, num_images)
                
if df_images is not None:
    print("Image loaded successfully")                
    # print(df_images.head(3))
    
else:
    print("Failed to load images...")
                
# 20.09 seconds - just for loading the data...        

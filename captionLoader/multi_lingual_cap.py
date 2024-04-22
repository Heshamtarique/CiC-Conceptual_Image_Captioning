# importing relevant libraries

import os
import json
# pip install opencv-python
import cv2
import numpy as np
import pandas as pd



# loading the Multi Lingual caption file...

def load_jsonl_file1(file_path):
    try:
        df = pd.read_json(file_path, lines=True)
        return df
    except Exception as e:
        print(f"Error loading JSONL file: {e}")
        return None

# Example usage:
file_path = "/User/multi_lingual_captions.jsonl"
df = load_jsonl_file1(file_path)
# df = pd.DataFrame(data)
# Check if DataFrame was successfully loaded
if df is not None:
    # Now you can use df for further data analysis
    print("DataFrame loaded successfully!")
    print(df.head())
else:
    print("Failed to load DataFrame.")


# analysis 
df.shape

df.columns

''' 
Index(['image/key', 'image/locale', 'ar', 'bn', 'cs', 'da', 'de', 'el', 'en',
       'es', 'fa', 'fi', 'fil', 'fr', 'hi', 'hr', 'hu', 'id', 'it', 'he', 'ja',
       'ko', 'mi', 'nl', 'no', 'pl', 'pt', 'quz', 'ro', 'ru', 'sv', 'sw', 'te',
       'th', 'tr', 'uk', 'vi', 'zh'],
      dtype='object')
'''
df_en = df[['image/key','en']]
df_en.tail(8)


###################### fetching the final caption from the dataset which is little processed
def fetch_caption(df):
    try:
        df['val_en'] = df['en'].apply(lambda x: x.get("caption/tokenized/lowercase") if isinstance(x, dict) else None)
    except Exception as e:
        print(f"Error: {e}")

# lets call it...
fetch_caption(df_en)

df_en.head(3)
final_caption_file = df_en.drop(columns=['en'])
final_caption_file.tail(3)




print(f"caption fora data in english:  {df_en['en'][3599]}")


import os
import gdown

path_weight = './model/ke_t5_dm/'

if not os.path.isdir(path_weight):
   os.makedirs(path_weight)
   

url = 'https://drive.google.com/file/d/1ZkU5psrtBaNwn7AWZ2XrOdv8P8CammlF/view?usp=share_link'
output = f'{path_weight}best.pt'
gdown.download(url, output, quiet=False, fuzzy=True)
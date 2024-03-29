import os
import gdown

path_weight = './model/ke_t5_dm/'

if not os.path.isdir(path_weight):
   os.makedirs(path_weight)
   

url = 'https://drive.google.com/file/d/13U0Dp6tfAGAw0fWQ_zdlWCvi_AdEhosh/view?usp=drive_link'
output = f'{path_weight}best.pt'
gdown.download(url, output, quiet=False, fuzzy=True)

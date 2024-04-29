import torch
from PIL import Image
import requests
from lavis.models import load_model_and_preprocess
import os

device = torch.device("cuda") if torch.cuda.is_available() else "cpu"
model, vis_processors, _ = load_model_and_preprocess(
     name="blip2_opt", model_type="pretrain_opt2.7b", is_eval=True, device=device
)

path = './emo/image/sadness'
filelist = os.listdir(path)

for name in filelist:
    print('-----------')
    print(name)
    out_path = './emo/caption/sadness/' + name.split('.')[0] + '.txt'
    f = open(out_path, 'w')
    raw_image = Image.open(path + name)
    image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
    
    caption = model.generate({"image": image})
    print(caption[0])
    f.write(caption[0])
    f.close()
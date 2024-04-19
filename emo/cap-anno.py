import os
import json

class_name = 'sadness'

path = './emo/caption/' + class_name + '/'
filelist = os.listdir(path)

caption_path = './emo/caption/' + class_name + '/'
annotation_path = './emo/annotation/' + class_name + '/'
for name in filelist:
    print(name)
    with open(caption_path + name, 'r', encoding='utf-8') as file:
        caption = file.read()
    with open(annotation_path + name.split('txt')[0] + 'json', 'r') as json_file:
        annotation = json.load(json_file)
        
    
    out = caption
    out = out + '\n\n'
    out = out + 'emotion: ' + str(annotation['emotion'])
    if 'brightness' in annotation:
        out = out + '\n' + 'brightness: ' + str(annotation['brightness'])
    if 'colorfulness' in annotation:
        out = out + '\n' + 'colorfulness: ' + str(annotation['colorfulness'])
      
    if 'object' in annotation:
        out = out + '\n' + 'object: ' + str(annotation['object'])
    if 'facial_expression' in annotation:
        out = out + '\n' + 'facial_expression: ' + str(annotation['facial_expression'])
    if 'human_action' in annotation:
        out = out + '\n' + 'human_action: ' + str(annotation['human_action'])
    
    out_path = "./emo/cap-ano/" + class_name + "/" + name
    f = open(out_path, 'w')
    f.write(out)
    f.close()
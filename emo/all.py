import json
import os
import re
import shutil
import random



out = []
# reasoning
folder_path_reasoning = './emo/reasoning/'
filelist_reasoning = os.listdir(folder_path_reasoning)

for class_name in filelist_reasoning:
    path = os.path.join(folder_path_reasoning, class_name)
    item = os.listdir(path)
    
    
    for name in item:
        with open(folder_path_reasoning + class_name + '/' + name, 'r', encoding='utf-8') as file:
            text = file.read()
        pattern = r"(?i)Question\s*:(.*?)\s*Answer\s*:(.*?)(?=\s*(Question\s*:|Answer\s*:|$))"

        matches = re.findall(pattern, text, re.DOTALL)
        reasoning = []

        for match in matches:
            question = match[0].strip()
            answer = match[1].strip()
            reasoning.append({"from": "human", "value": question})
            reasoning.append({"from": "gpt", "value": answer})
        
        
        for i in range(int(len(reasoning)/2)):
            out.append({"id": name.split('_')[1][:5], "image": name.split('.')[0] + '.jpg', 'conversations': reasoning[2*i:2*i+2]})


# conversation

folder_path = './emo/conversation/'
filelist = os.listdir(folder_path)
for class_name in filelist:
    path = os.path.join(folder_path, class_name)
    item = os.listdir(path)
    
    
    for name in item:
        with open(folder_path + class_name + '/' + name, 'r', encoding='utf-8') as file:
            text = file.read()
    
        pattern = r"(?i)Question\s*\d*:(.*?)\s*Answer\s*\d*:(.*?)\s*(?=(Question:\d*|Complex Question:\d*|Complex question:\d*|$))"
        matches = re.findall(pattern, text, re.DOTALL)
        conversations = []

        for match in matches:
            question = match[0].strip()
            answer = match[1].strip()
            conversations.append({"from": "human", "value": question})
            conversations.append({"from": "gpt", "value": answer})
        
        
        conversations[0]['value'] = conversations[0]['value']
        
        for i in range(int(len(conversations)/2)):
            out.append({"id": name.split('_')[1][:5], "image": name.split('.')[0] + '.jpg', 'conversations': conversations[2*i:2*i+2]})

        shutil.copy('./emo/image/' + class_name + '/' + name[:-3] + 'jpg', './emo/image/all_reasoning')



# conversation100
folder_path = './emo/conversation_new100/'
filelist = os.listdir(folder_path)
for class_name in filelist:
    path = os.path.join(folder_path, class_name)
    item = os.listdir(path)
    
    
    for name in item:
        with open(folder_path + class_name + '/' + name, 'r', encoding='utf-8') as file:
            text = file.read()
    
        pattern = r"(?i)Question\s*\d*:(.*?)\s*Answer\s*\d*:(.*?)\s*(?=(Question:\d*|Complex Question:\d*|Complex question:\d*|$))"
        matches = re.findall(pattern, text, re.DOTALL)
        conversations = []

        for match in matches:
            question = match[0].strip()
            answer = match[1].strip()
            conversations.append({"from": "human", "value": question})
            conversations.append({"from": "gpt", "value": answer})
        
        
        conversations[0]['value'] = conversations[0]['value']
        
        for i in range(int(len(conversations)/2)):
            out.append({"id": name.split('_')[1][:5], "image": name.split('.')[0] + '.jpg', 'conversations': conversations[2*i:2*i+2]})

        shutil.copy('./emo/image/' + class_name + '/' + name[:-3] + 'jpg', './emo/image/all_reasoning')
        
        
##### classification  
with open('./emo/train.json', 'r') as json_file:
    json_data = json.load(json_file)
    
amusement_data = []
anger_data = []
awe_data = []
contentment_data = []
disgust_data = []
excitement_data = []
fear_data = []
sadness_data = []
    
for item in json_data:
    category = item[0]
    if category == 'amusement':
        amusement_data.append(item[1].split('/')[2][:-4])
    elif category == 'anger':
        anger_data.append(item[1].split('/')[2][:-4])
    elif category == 'awe':
        awe_data.append(item[1].split('/')[2][:-4])
    elif category == 'contentment':
        contentment_data.append(item[1].split('/')[2][:-4])
    elif category == 'disgust':
        disgust_data.append(item[1].split('/')[2][:-4])
    elif category == 'excitement':
        excitement_data.append(item[1].split('/')[2][:-4])
    elif category == 'fear':
        fear_data.append(item[1].split('/')[2][:-4])
    elif category == 'sadness':
        sadness_data.append(item[1].split('/')[2][:-4])

all_data = [amusement_data, anger_data, awe_data, contentment_data, disgust_data, excitement_data, fear_data, sadness_data]
emo = ['amusement', 'anger', 'awe', 'contentment', 'disgust', 'excitement', 'fear', 'sadness']

for i in range(8):
    for j in range(700, 5600):
        word = [
          {
            "from": "human",
            "value": "Please select the emotion closest to the image from the following options:\
amusement, \
anger, \
awe, \
contentment, \
disgust, \
excitement, \
fear and sadness \
(Do not provide answers outside of the candidates options.) Please answer in the following format:  Predict emotion:"
          },
          {
            "from": "gpt",
            "value": 'Predict emotion: ' + emo[i]
          }
        ]
        temp = {'id': all_data[i][j][-5:], 'image': all_data[i][j] + '.jpg', 'conversations': word}
        
        out.append(temp)
        
        shutil.copy('./emo/image/' + emo[i] + '/' + all_data[i][j] + '.jpg', './emo/image/all_reasoning')
#####
# conversationturbo

folder_path = './emo/conversation_turbo/'
filelist = os.listdir(folder_path)
for class_name in filelist:
    path = os.path.join(folder_path, class_name)
    item = os.listdir(path)
    
    
    for name in item:
        with open(folder_path + class_name + '/' + name, 'r', encoding='utf-8') as file:
            text = file.read()
    
        pattern = r"(?i)Question\s*\d*:(.*?)\s*Answer\s*\d*:(.*?)\s*(?=(Question:\d*|Complex Question:\d*|Complex question:\d*|$))"
        matches = re.findall(pattern, text, re.DOTALL)
        conversations = []

        for match in matches:
            question = match[0].strip()
            answer = match[1].strip()
            conversations.append({"from": "human", "value": question})
            conversations.append({"from": "gpt", "value": answer})
        
        
        conversations[0]['value'] = conversations[0]['value']
        
        for i in range(int(len(conversations)/2)):
            out.append({"id": name.split('_')[1][:5], "image": name.split('.')[0] + '.jpg', 'conversations': conversations[2*i:2*i+2]})all
        
            
random.shuffle(out)
with open('./emo/all.json', 'w') as json_file:
    json.dump(out, json_file, indent=2)
    

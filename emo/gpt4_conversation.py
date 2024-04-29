import requests
import json
import openai
import os

#openai.api_key need to change to your own key
#Search "Need change!!!" in this script
#Change the number in range


def generate_chat_completion(messages, model="gpt-4", temperature=1, max_tokens=None):
    openai.api_key =""

    
    response = openai.ChatCompletion.create(
                   model="gpt-4",
                   max_tokens=None,
                   temperature=1,
                   messages = messages)

    return response["choices"][0]["message"]["content"]


#####
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
        
#####

prompt_path = "./emo/prompt/conversation.txt"
with open(prompt_path, 'r', encoding='utf-8') as file:
    content = file.read()


#Need change!!!
class_name = 'sadness'
filelist = sadness_data


path = './emo/cap-ano/' + class_name + '/'
for i in range(1000, 1100):
    print(i)
    name = filelist[i]
    caption_path = "./emo/cap-ano/" + class_name + "/" + name + '.txt'
    with open(caption_path, 'r', encoding='utf-8') as file:
        caption = file.read()

    messages = [
        {"role": "system", "content": content},
        {"role": "user", "content": caption}
    ]

    response_text = generate_chat_completion(messages)


    out_path = "./emo/conversation_new100/" + class_name + "/" + name + '.txt'
    f = open(out_path, 'w')
    f.write(response_text)
    f.close()
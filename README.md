# EmoVIT
Official code for paper EmoVIT: Revolutionizing Emotion Insights with Visual Instruction Tuning ｜ CVPR 2024

```
EmoSet/
|
+--LAVIS
|
+--emo
    |
    +--annotation
    |
    +--cap-ano
    |
    +--caption
    |
    +--prompt
    |
    +--image
        +--amusement (Results of Emoset Decompression)
        |
        +--anger (Results of Emoset Decompression)
        |
        .
        .
        .
        |
        +--result_image
                |
                ........
```
You can find two main folders in our project structure, 'emo' and 'LAVIS'.  
The 'emo' folder can be obtained from https://drive.google.com/file/d/1zSZZa7_3mzzhVDlka4GYyJHJrLR5F7vN/view?usp=drive_link , 
while the 'LAVIS' folder can be obtained from https://drive.google.com/file/d/1nNa0fGU3gsgK07b6eJpUJ4Fu8mx_Xlrt/view?usp=drive_link .
Arrange the image data into the correct locations as described above. For example, EmoSet can be obtained from https://vcc.tech/EmoSet.

## Install related packages
conda create --name emovit python=3.8  
conda activate emovit  
cd emovit  
pip install -r requirements.txt  

## Install lavis
pip install salesforce-lavis  
(If not work, please proceed as follows.)  
cd ..  
git clone https://github.com/salesforce/LAVIS.git  
cd LAVIS  
pip install -e . (Please remove 'open3d' from the 'requirements.txt' file to avoid version conflicts.)  
Cut the 'lavis' folder and paste it into the 'lib' folder.  

## caption
1. python ./emo/caption.py (To obtain image captions，select the 'path' based on the class to be processed.) 
2. python ./emo/cap-anno.py (To write the attributes and captions of the image into a file，select the 'path' based on the class to be processed.)  
3. python ./emo/gpt4_reasoning.py or python ./emo/gpt4_conversation.py (Using the above file as input data, instruct gpt4 to generate questions.)  
#Remember to change the key  
#If you wish to adjust the prompt, you can go to the 'prompt' folder.
4. python ./emo/all.py (Integrate the results of reasoning, conversation, and classification.)

## Train emoVIT 
- Prepare weight  
  You can obtain the weights for Vicuna from the page https://github.com/lm-sys/FastChat/blob/main/docs/vicuna_weights_version.md , we are using version 1.1.
  Place the downloaded file into LAVIS/lavis/weight/vicuna-7b-2/
  
- Run  
    - training  
    python train.py --cfg-path FT.yaml  

    - inference  
    the use of testing are in inference.py  

- Parameter  
  LAVIS/FT.yaml (Setting of hyperparameter)  
  LAVIS/lavis/configs/models/blip2/blip2_instruct_vicuna7b.yaml (Select the location of llm weight)  
  LAVIS/lavis/configs/datasets/coco/defaults_vqa.yaml (Select the location of your data)  

## Inference emoVIT
If you haven't trained your own weights yet, you can use the model_weights1.pth provided in the LAVIS folder. 
python ./LAVIS/test.py  

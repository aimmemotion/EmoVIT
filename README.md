# EmoVIT
Official code for the paper **"EmoVIT: Revolutionizing Emotion Insights with Visual Instruction Tuning"** | CVPR 2024

```
EmoSet/
|
+--LAVIS
|
+--emo
    |
    +--annotation (Results of EmoSet decompression.)
    |
    +--cap-ano (Create the folders required for program execution before running it.)
    |
    +--caption (Create the folders required for program execution before running it.)
    |
    +--reasoning (Create the folders required for program execution before running it.)
    |
    +--conversation_new100 (Create the folders required for program execution before running it.)
    |
    +--prompt
    |
    +--image
        +--amusement (Results of EmoSet decompression)
        |
        +--anger (Results of EmoSet decompression)
        |
        .
        .
        .
        |
        +--train_image (EmoVIT does not need all photos; place the photos required for training here.)
                |
                ........
```

You can find two main folders in our project structure: `emo` and `LAVIS`.

- The `LAVIS` folder can be obtained from [here](https://drive.google.com/file/d/1YLgOVlJNIdyOOlppX0uPMXGxVT37YqbF/view?usp=drive_link).
- Arrange the image data into the correct locations as described above. For example, EmoSet can be obtained from [EmoSet](https://vcc.tech/EmoSet).

## Install Related Packages

```bash
conda create --name emovit python=3.8
conda activate emovit
cd emovit
pip install -r requirements.txt
```

## Install LAVIS

```bash
pip install salesforce-lavis
# If not work, please proceed as follows.
cd ..
git clone https://github.com/salesforce/LAVIS.git
cd LAVIS
pip install -e . # Please remove 'open3d' from the 'requirements.txt' file to avoid version conflicts.
# Cut the 'lavis' folder and paste it into the 'lib' folder.
```

## Generate Captions

1. Run `python ./emo/caption.py` to obtain image captions. Select the 'path' based on the class to be processed.
2. Run `python ./emo/cap-anno.py` to write the attributes and captions of the image into a file. Select the 'path' based on the class to be processed.
3. Run `python ./emo/gpt4_reasoning.py` or `python ./emo/gpt4_conversation.py` to instruct GPT-4 to generate questions using the above file as input data.
    - Remember to change the key.
    - If you wish to adjust the prompt, you can go to the 'prompt' folder.
4. Run `python ./emo/all.py` to integrate the results of reasoning, conversation, and classification.

Following these steps, you can create instructions. If you want to skip this step, you can use the instructions we created using EmoSet. (However, image data must still be downloaded from EmoSet's official website.)

- Conversation: [Download](https://drive.google.com/file/d/1E8UEH09y0CiAT4Hg7rm975AR3JCjEHeM/view?usp=drive_link)
- Reasoning: [Download](https://drive.google.com/file/d/1MTNHFzasCb0F921P0itaH-x8vN2OvxEu/view?usp=drive_link)

The generation method of categorical data does not need to rely on GPT for creation; it can be directly produced (you can observe the prompt in `all.py`).

## Train EmoVIT

### Prepare Weights

You can obtain the weights for Vicuna from [this page](https://github.com/lm-sys/FastChat/blob/main/docs/vicuna_weights_version.md). We are using version 1.1. Place the downloaded file into `LAVIS/lavis/weight/vicuna-7b-2/`.

### Run

#### Training

```bash
cd LAVIS
python train.py --cfg-path FT.yaml
```

### Parameter Settings

- `LAVIS/FT.yaml`: Setting of hyperparameters
- `LAVIS/lavis/configs/models/blip2/blip2_instruct_vicuna7b.yaml`: Select the location of LLM weight
- `LAVIS/lavis/configs/datasets/coco/defaults_vqa.yaml`: Select the location of your data
  LAVIS/lavis/runners/runner_base.py (Change the name of the weight file to be saved.)

## Inference emoVIT
If you haven't trained your own weights yet, you can use the `model_weights1.pth` provided in the `LAVIS` folder.  
```bash
python ./LAVIS/test.py  
```


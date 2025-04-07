# Update 2025/04/07
Some parts of the code were using wrong version parameters, which caused issues during inference.
Several related parameter files have been updated—you can find them in the main folder. Please replace the original files with these updated versions.

Both FT.yaml and blip2_vicuna_instruct have been modified to use the correct parameters.
(Note: blip2_vicuna_instruct should be placed under LAVIS/lavis/models/blip2_models.)

The train.json file originally provided was incomplete; the current version contains the full dataset.
https://drive.google.com/file/d/1OV3X7BJyEDYXTGaDbu7E8rGgGzIlnwVq/view?usp=drive_link

As for the weights trained with the correct parameters, you can download them from the following link:
https://drive.google.com/file/d/1zaYOSlt3mLVMdiNfAKdJcwvVc-4LHfdr/view?usp=drive_link"

# EmoVIT
Official code for the paper **"EmoVIT: Revolutionizing Emotion Insights with Visual Instruction Tuning"** | CVPR 2024

## Setting up the environment

```bash
git clone https://github.com/aimmemotion/EmoVIT.git
conda create --name emovit python=3.8
conda activate emovit

cd Emovit
pip install -r requirements_lavis.txt
```
## Install the corresponding version of PyTorch

```bash
#Using CUDA 11.8 as an example
pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
```

## Install LAVIS

```bash
pip install salesforce-lavis
# If not work, please proceed as follows.
cd ..
git clone https://github.com/salesforce/LAVIS.git
cd LAVIS
pip install -e . # Please remove 'open3d' from the 'requirements.txt' file to avoid version conflicts.
cd ../
# Cut the 'lavis' folder and paste it into the 'lib' folder.
```

## Dataset Preparation

Download EmoSet from
https://vcc.tech/EmoSet

Extract the downloaded EmoSet files
(annotation, image, info.json, test.json, train.json, val.json)
and place them into the emo folder.


## Model Preparation

Download lavis_with_weight.zip https://drive.google.com/file/d/1vZa7C6rxxsq51VQ73ESGQ0S8zEI2dnq_/view?usp=drive_link
(If you prefer to train it yourself, you can download lavis_without_weight.zip instead https://drive.google.com/file/d/1Re_lzyrQehuL1SjP4GmgPCMPf5jHg3hs/view?usp=drive_link)
Extract the zip file and place it in the emovit folder.

Download all files from this Hugging Face page
https://huggingface.co/lmsys/vicuna-7b-v1.1/tree/main
Place the downloaded files into ./Emovit/LAVIS/lavis/weight/vicuna-7b-2/

## Emotion Instruction Data Generation

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

## Inference EmoVIT
If you haven't trained your own weights yet, you can use the `model_weights1.pth` provided in the `LAVIS` folder.  
```bash
python ./LAVIS/test.py  
```

## Citation

If you found this paper is helpful, please consider cite our paper:

```bibtex
@inproceedings{Xie2024EmoVIT,
  title={EmoVIT: Revolutionizing Emotion Insights with Visual Instruction Tuning},
  author={Hongxia Xie and Chu-Jun Peng and Yu-Wen Tseng and Hung-Jen Chen and Chan-Feng Hsu and Hong-Han Shuai and Wen-Huang Cheng},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2024}
}
```

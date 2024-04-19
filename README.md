# EmoVIT
Official code for paper EmoVIT: Revolutionizing Emotion Insights with Visual Instruction Tuning ｜ CVPR 2024

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

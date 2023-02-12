import os
from os import path as osp
import numpy as np

get_dir='./data/aerial/dataset/semantic_drone_dataset/label_images_semantic'
txt_save_in='./data/aerial/dataset/semantic_drone_dataset/'
need_txt=['train.txt','val.txt','test.txt']
all_scale_list=np.array([8,2,0])
all_scale_list=all_scale_list/all_scale_list.sum()

files_list=os.listdir(get_dir)
np.random.shuffle(files_list)
sum=0
start=0
end=0
for ind,ratio in enumerate(all_scale_list):
    sum += all_scale_list[ind]
    end=int(sum*len(files_list))
    save_list=files_list[start:end]
    start=end
    with open(osp.join(txt_save_in,need_txt[ind]), 'w') as f:
        f.writelines(line.split('.')[0] + '\n' for line in save_list)
import os
from os import path as osp
import shutil
import numpy as np

get_dir='./flower_dataset/'
need_dir=['train','val','test']
all_scale_list=np.array([8,2,0])
all_scale_list=all_scale_list/all_scale_list.sum()

for dir in need_dir:
    dir=osp.join(get_dir,dir)
    if osp.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)
for from_dir in os.listdir(get_dir):
    if from_dir in need_dir:
        continue
    files_list=os.listdir(osp.join(get_dir,from_dir))
    np.random.shuffle(files_list)
    start=0
    sum=0
    for ind,dir in enumerate(need_dir):
        os.makedirs(osp.join(get_dir,dir,from_dir))
        sum+=all_scale_list[ind]
        end=int(sum*len(files_list))
        for file in files_list[start:end]:
            shutil.copy(osp.join(get_dir,from_dir,file),osp.join(get_dir,dir,from_dir,file))
        start=end
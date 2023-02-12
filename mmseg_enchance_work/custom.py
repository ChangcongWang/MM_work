from mmseg.registry import DATASETS
from mmseg.datasets import BaseSegDataset
classes = ['unlabeled', 'paved-area', 'dirt', 'grass', 'gravel', 'water', 'rocks', 'pool',
 'vegetation', 'roof', 'wall', 'window', 'door', 'fence', 'fence-pole', 'person',
  'dog', 'car', 'bicycle', 'tree', 'bald-tree', 'ar-marker', 'obstacle', 'conflicting'] 
palette = [[0, 0, 0], [128, 64, 128], [0, 76, 130], [0, 102, 0], [87, 103, 112], [168, 42, 28],
 [30, 41, 48], [89, 50, 0], [35, 142, 107], [70, 70, 70], [156, 102, 102], [12, 228, 254],
  [12, 148, 254], [153, 153, 190], [153, 153, 153], [96, 22, 255], [0, 51, 102], [150, 143, 9],
   [32, 11, 119], [0, 51, 51], [190, 250, 190], [146, 150, 112], [115, 135, 2], [0, 0, 255]] 
@DATASETS.register_module()
class CustomDataset(BaseSegDataset):
  METAINFO = dict(classes = classes, palette = palette)
  def __init__(self, **kwargs):
    super().__init__(img_suffix='.jpg', seg_map_suffix='.png', **kwargs)

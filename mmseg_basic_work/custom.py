from mmseg.registry import DATASETS
from mmseg.datasets import BaseSegDataset
classes = ('background', 'crack')
palette = [[0,0,0], [87,87,87]]
@DATASETS.register_module()
class CustomDataset(BaseSegDataset):
  METAINFO = dict(classes = classes, palette = palette)
  def __init__(self, **kwargs):
    super().__init__(img_suffix='.png', seg_map_suffix='.png', **kwargs)

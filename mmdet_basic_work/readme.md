# MMDet 基础作业
## 实验设备
GTX2070 Mobile

MMDet 2.28
## 模型指标
|Model|	bbox_map	|bbox_map@50	|bbox_map@75	|Config	|
|-|	-|-	|-|-	|
|mask_rcnn_r101_fpn_mstrain-poly_3x_ballon	|0.7685|	0.8749|	0.8519	|[config](./mask_rcnn_r101_fpn_mstrain-poly_3x_ballon.py)|
## 模型下载地址
有点大，抱歉了
```
链接: https://pan.baidu.com/s/1Fr1o6ESTqQ1e66-Y2WZNfg 提取码: mmcv 复制这段内容后打开百度网盘手机App，操作更方便哦
```
## 常见错误
The testing results of the whole dataset is empty.
原因为学习率设置过大
建议使用 Instance Segmentation 列的检测方法进行检测，Object Detection的检测方法较差。经常错检漏检
## 效果图
![效果图](./color_splash.gif)
# Refers to https://pytorch.org/blog/ml-models-torchvision-v0.9/#classification

_base_ = [
    '../_base_/models/mobilenet_v3/mobilenet_v3_large_imagenet.py',
    '../_base_/datasets/cifar10_bs16.py',
    '../_base_/schedules/cifar10_bs128.py',
    '../_base_/default_runtime.py',
]

train_cfg = dict(by_epoch=True, max_epochs=300, val_interval=1)
val_cfg = dict()
test_cfg = dict()

load_from='mobilenet-v3-large_8xb128_in1k_20221114-0ed9ed9a.pth'
train_dataloader = dict(batch_size=128)
val_dataloader = dict(batch_size=128)
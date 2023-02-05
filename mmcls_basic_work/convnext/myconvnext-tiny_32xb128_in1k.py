_base_ = [
    '../_base_/models/convnext/convnext-tiny.py',
    '../_base_/datasets/imagenet_bs64_swin_224.py',
    '../_base_/schedules/imagenet_bs1024_adamw_swin.py',
    '../_base_/default_runtime.py',
]

model = dict(
    head=dict(
        num_classes=5,
        topk=(1)))

data = dict(
    samples_per_gpu=32,
    workers_per_gpu=2,
    train=dict(
        type='CustomDataset',
        data_prefix='data/flower_dataset/train'
    ),
    val=dict(
        type='CustomDataset',
        data_prefix='data/flower_dataset/val',
        ann_file=None,
    ),
    test=dict(
        type='CustomDataset',
        data_prefix='data/flower_dataset/val',
        ann_file=None,
    ))
evaluation = dict(interval=1, metric='accuracy')

optimizer = dict(lr=1e-3)

custom_hooks = [dict(type='EMAHook', momentum=4e-5, priority='ABOVE_NORMAL')]

runner = dict(type='EpochBasedRunner', max_epochs=100)

load_from = 'convnext-tiny_3rdparty_32xb128_in1k_20220124-18abde00.pth'
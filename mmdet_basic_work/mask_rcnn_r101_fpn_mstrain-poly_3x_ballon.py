_base_ = [
    '../common/mstrain-poly_3x_coco_instance.py',
    '../_base_/models/mask_rcnn_r50_fpn.py'
]

model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=1
        ),
        mask_head=dict(
            num_classes=1
        )
    ),

    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))

classes=('balloon',)
optimizer=dict(lr=0.003)
# runner = dict(type='EpochBasedRunner', max_epochs=30)

data = dict(
    samples_per_gpu=1,
    workers_per_gpu=1,
    train=dict(
        dataset=dict(
            type='CocoDataset',
            classes=classes,
            ann_file='data/balloon/train/train_ann.json',
            img_prefix='data/balloon/train/')
    ),
    val=dict(
            type='CocoDataset',
            classes=classes,
            ann_file='data/balloon/val/val_ann.json',
            img_prefix='data/balloon/val/'),
    test=dict(
            type='CocoDataset',
            classes=classes,
            ann_file='data/balloon/val/val_ann.json',
            img_prefix='data/balloon/val/')
)
# max_epochs=30
load_from='mask_rcnn_r50_fpn_mstrain-poly_3x_coco_20210524_201154-21b550bb.pth'
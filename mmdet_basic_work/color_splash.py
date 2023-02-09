# 参考https://github.com/aso538/OpenMMLab_AI_camp_work/blob/main/basic_wor_2/color_splash.py
import cv2
import mmcv
import numpy as np
from mmdet.apis import init_detector,inference_detector,show_result_pyplot


video=mmcv.VideoReader('./test_video.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(
    './color_splash.mp4', fourcc, video.fps,
    (video.width, video.height))
config_file="configs/mask_rcnn/mask_rcnn_r101_fpn_mstrain-poly_3x_ballon.py"
checkpoint_file="work_dirs/mask_rcnn_r101_fpn_mstrain-poly_3x_ballon/epoch_12.pth"

model=init_detector(config_file,checkpoint_file)
thr=0.8
# frame_one=None
# frames=[]
for frame in video:
    result=inference_detector(model,frame)
    masks=result[1][0]
    check_mask=np.full((frame.shape[0], frame.shape[1]), False)
    for ind,mask in enumerate(masks):
        if result[0][0][ind][-1]>thr:
            check_mask = np.logical_or(check_mask,mask)

    mask_frame=np.zeros_like(frame)
    for ind in range(3):
        mask_frame[:,:,ind]=frame[:,:,ind]*check_mask
    
    frame=frame-mask_frame
    gray_frame=mmcv.bgr2gray(frame,keepdim=True)
    frame=gray_frame+mask_frame
    video_writer.write(frame)
#     if frame_one is None:
#         frame_one=frame
#     else:
#         frames.append(frame)

# frame_one.save("flask_demo.gif", format="GIF", append_images=frames,
#                    save_all=True, duration=1000/video.fps, loop=0)

video_writer.release()
cv2.destroyAllWindows()

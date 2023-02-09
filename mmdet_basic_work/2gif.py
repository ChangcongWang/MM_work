from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("./mmdet_basic_work/color_splash.mp4").resize(0.5)

videoClip.write_gif("./mmdet_basic_work/color_splash.gif",)
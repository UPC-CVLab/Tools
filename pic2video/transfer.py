import cv2
import os

im_dir = './pics'  # 图片存储路径
video_dir = './a.avi' # 视频存储路径及视频名
fps = 20 # 帧率一般选择20-30
num = 1001 # 图片数+1，因为后面的循环是从1开始
img_size = (512,512) # 图片尺寸，若和图片本身尺寸不匹配，输出视频是空的

fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)

for i in range(1,num):
    im_name = os.path.join(im_dir, str(i).zfill(6)+'.jpg')
    frame = cv2.imread(im_name)
    videoWriter.write(frame)
    print(im_name)

videoWriter.release()
print('finish')
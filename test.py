

#load data
import json

file='./data/05/false_changapqua_01.json'
# file='./data/05/true_01.json'
data=json.load(open(file))


def predict_05(frame):
    if abs(data[frame_id]['LKnee'][0]-data[frame_id]['LBigToe'][0])>10:
        return False
    else:
        return True

output=[]
for frame_id in data:
    ans=predict_05(data[frame_id])
    output.append(ans)
    # print(ans)


import numpy as np
import cv2
import os

videopath='./data/05/' + os.path.basename(file)[:-4] + 'avi'
def readframe(video_path,frame_count):
    cap = cv2.VideoCapture(video_path)
    i=0
    while(cap.isOpened()):
        i+=1
        ret, frame = cap.read()
        if i==frame_count:
            cap.release()
            return frame
    cap.release()
    return None


print(output)
count_true=0
for ans in output:
    if ans ==True:
        count_true+=1
print(count_true,len(output)-count_true)
# frame_count=0
# for ans in output:
#     if not ans:
#         frame=readframe(videopath,frame_count)
#         frame=cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))
#         cv2.imshow('frame', frame)
#         cv2.waitKey(10)
#     frame_count+=1
#
# cv2.destroyAllWindows()




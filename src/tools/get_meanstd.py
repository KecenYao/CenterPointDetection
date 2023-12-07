import os
import numpy as np
import cv2

BGR = True    # the order of mean and std
img_h, img_w = 512, 512   # the same as training setting
means, stdevs = [], []
img_list = []
 
imgs_path = ''   # to be filled
imgs_path_list = os.listdir(imgs_path)
 
len_ = len(imgs_path_list)
i = 0
for item in imgs_path_list:
    img = cv2.imread(os.path.join(imgs_path,item))
    img = cv2.resize(img, (img_w, img_h))
    img = img[:, :, :, np.newaxis]
    img_list.append(img)
    i += 1
    print(i,'/',len_)    
 
imgs = np.concatenate(img_list, axis=3)
imgs = imgs.astype(np.float32) / 255.
 
for i in range(3):
    pixels = imgs[:, :, i, :].ravel()  # to be one line
    means.append(np.mean(pixels))
    stdevs.append(np.std(pixels))
 
if BGR:
    print('Order in BGR')
    print("normMean = {}".format(means))
    print("normStd = {}".format(stdevs))
else:
    means.reverse()
    stdevs.reverse()
    print('Order in RGB')
    print("normMean = {}".format(means))
    print("normStd = {}".format(stdevs))
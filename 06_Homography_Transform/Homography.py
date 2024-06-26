import cv2
import numpy as np
import matplotlib.pyplot as plt

from skimage import transform
from skimage.io import imread, imshow

Obj = imread('Chess.jpg')

Obj = cv2.cvtColor(Obj, cv2.COLOR_BGR2RGB)

a = [413, 242,
     76, 1587,
     2534, 1579,
     2187, 228]

src = np.array(a).reshape((-1, 2))  # n row 2 col

# plt.scatter(src[:, 0], src[:, 1], color='red', marker='*')
# plt.imshow(Obj)
# plt.show()
print(Obj.shape[0], Obj.shape[1], Obj.shape[0], Obj.shape[1])


dst = np.array([0, 0,
                0, Obj.shape[0],
                Obj.shape[1], Obj.shape[0],
                Obj.shape[1], 0]).reshape((4, 2))

tform = transform.estimate_transform('projective', src, dst)

tf_img = transform.warp(Obj, tform.inverse, output_shape=(Obj.shape[0], Obj.shape[1]))

fig, ax = plt.subplots()
ax.imshow(tf_img)
ax.set_title('Projective Transformation')

plt.show()

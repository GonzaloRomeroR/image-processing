import cv2
import numpy as np
from matplotlib import pyplot as plt
def deskew(img):
    SZ = 500
    m = cv2.moments(img)
    if abs(m['mu02']) < 1e-2:
        # no deskewing needed.
        return img.copy()
    # Calculate skew based on central momemts.
    skew = m['mu11']/m['mu02']
    #skew = -1
    print(skew)
    # Calculate affine transform to correct skewness.
    M = np.float32([[1, skew, -0.5*len(img)*skew], [0, 1, 0]])
    # Apply affine transform
    #img = cv2.warpAffine(img, M, (len(img[0]), len(img)), flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)
    rows,cols = img.shape


    img = cv2.imread('messi5.jpg',0)
    edges = cv2.Canny(img,100,200)

    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()

img = cv2.imread('tornillo0.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
imga = deskew(img)
cv2.imshow('image',imga)
cv2.waitKey(0)
cv2.destroyAllWindows()

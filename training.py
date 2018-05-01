import cv2
import numpy as np
import os

def imageProcessing(image):
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(image,None)
    img = cv2.drawKeypoints(image, kp, image)
    cv2.imwrite('sift_keypoints.jpg', img)
    print (kp)
    input ('')


def train():
    for subdirectorie in os.listdir("training"):
        path = "training/" + subdirectorie
        for j in range(len(os.listdir(path))):
            print (subdirectorie + str(j) + ".jpg")
            imageName = subdirectorie + str(j) + ".jpg"
            image = cv2.imread(path + "/" + imageName, 0)
            if image is None:
                print("Image not found")
            else:
                imageProcessing(image)

def main():
    train()

if __name__ == '__main__':
    main()

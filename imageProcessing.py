# Image as input and features array as output

import cv2
import numpy as np
import os
import math

def imageProcessing(image):
    # Steps to process the image
    preImage = preprocessing(image)
    features = featureExtraction(preImage)
    return features

def preprocessing(image):
    # Gaussian filter applied
    blurImage = cv2.GaussianBlur(image,(5,5),0)
    # Convert to grayscale
    grayImage = cv2.cvtColor(blurImage, cv2.COLOR_BGR2GRAY)
    # Reduce image's size
    imageScaleFactor = 0.5
    preimage = cv2.resize(grayImage, None, fx= imageScaleFactor, fy= imageScaleFactor,
        interpolation= cv2.INTER_LINEAR)
    image = preimage
    # Binary image, black and white
    ret,binaryImage = cv2.threshold(preimage,70,255,cv2.THRESH_BINARY_INV)
    # Opening. Morphological transformation to clean the image
    #binaryImage = cv2.morphologyEx(binaryImage, cv2.MORPH_OPEN, (5,5))
    # Dilate the image to get cleaner contours
    kernel = np.ones((10,10),np.uint8)
    contourBinaryImage = cv2.dilate(binaryImage,kernel,iterations = 1)
    # Get contours
    im, contours, hierarchy = cv2.findContours(contourBinaryImage,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    # x,y,w,h = cv2.boundingRect(cnt)
    # preimage = cv2.rectangle(preimage,(x,y),(x+w,y+h),(0,255,0),2)
    # Get rectangule of smaller area and its edges
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    # im = cv2.drawContours(preimage,[box],0,(0,0,255),2)
    #preimage = preimage[[box]]
    preimage = cv2.cvtColor(preimage ,cv2.COLOR_GRAY2BGR)
    # preimage = cv2.drawContours(preimage, contours,-1, (250,0,0), 2)
    # Get angel to rotate
    angle = rect[2]
    if angle < -45:
        angle = angle - 90
    rows, cols, ch = preimage.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
    preimage = cv2.warpAffine(preimage, M, (cols,rows))

    # Rotate binary image in the same angle
    rows, cols= contourBinaryImage.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
    contourBinaryImage = cv2.warpAffine(contourBinaryImage, M, (cols,rows))
    # Find contours of the binary image
    im, contours, hierarchy = cv2.findContours(contourBinaryImage,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # Get minumum area rectangle
    cnt = contours[0]
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    # Cut image to paste in white image with given size
    preimage = preimage[int(box[1][1]):int(box[0][1]), int(box[0][0]):int(box[2][0])]
    ret,whiteImage = cv2.threshold(image,255,255,cv2.THRESH_BINARY_INV)
    preimage = cv2.cvtColor(preimage ,cv2.COLOR_BGR2GRAY)
    ret,preimage = cv2.threshold(preimage,70,255,cv2.THRESH_BINARY)
    # Insert image in white image
    maxRows, maxCols = whiteImage.shape
    rows, cols= preimage.shape
    whiteImage[int(maxRows/2 - rows/2) : int(maxRows/2 + rows/2), int(maxCols/2 - cols/2) : int(maxCols/2 +cols/2)] = preimage
    preimage = whiteImage


    ############## Debug ####################
    #Comment in case you don't need to debug
    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow('image', preimage )
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #########################################
    return preimage

def featureExtraction(image):
    # Obtain HOG's feature array
    features = HOG(image)
    return features

def HOG(image):
    # HOG's parameters
    winSize = (len(image[0]),len(image))
    blockSize = (int(len(image[0])/4), int(len(image)/4))
    blockStride = (int(len(image[0])/8), int(len(image)/8))
    cellSize = (int(len(image[0])/4), int(len(image)/4))
    nbins = 9
    derivAperture = 1
    winSigma = -1.
    histogramNormType = 0
    L2HysThreshold = 0.2
    gammaCorrection = 1
    nlevels = 64
    signedGradients = True
    hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize
        ,nbins,derivAperture,winSigma,histogramNormType,L2HysThreshold,
            gammaCorrection,nlevels, signedGradients)
    # Create HOG's descriptor
    descriptor = hog.compute(image)
    return descriptor

def main():
    pass

if __name__ == '__main__':
    main()

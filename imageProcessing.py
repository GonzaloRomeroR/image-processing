# Image as input and features array as output

import cv2
import numpy as np
import os

def imageProcessing(image):
    # Steps to process the image
    preImage = preprocessing(image)
    features = featureExtraction(preImage)
    return features

def preprocessing(image):
    # Reduce image's size
    imageScaleFactor = 0.5
    preimage = cv2.resize(image, None, fx= imageScaleFactor, fy= imageScaleFactor,
        interpolation= cv2.INTER_LINEAR)
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

import cv2
import numpy as np
import os

def imageProcessing(image):
    preImage = preprocessing(image)
    features = featureExtraction(preImage)
    return features


def preprocessing(image):
    factorEscalaImagen = 0.25
    preimage = cv2.resize(image, None, fx= factorEscalaImagen, fy= factorEscalaImagen,
        interpolation= cv2.INTER_LINEAR)
    return preimage

def featureExtraction(image):
    features = HOG(image)
    return features

def HOG(image):
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
    descriptor = hog.compute(image)
    return descriptor


def train():
    for subdirectory in os.listdir("training"):
        exec("%s = []" % subdirectory)
        path = "training/" + subdirectory
        for j in range(len(os.listdir(path))):

            imageName = subdirectory + str(j) + ".jpeg"
            image = cv2.imread(path + "/" + imageName, 0)
            if image is None:
                print("Image" + subdirectory + str(j) + ".jpeg" +" not found")
            else:
                print (subdirectory + str(j) + ".jpeg" + " done")
                procImage = imageProcessing(image)
                exec("%s.append(procImage)" % subdirectory)
        exec("npImage = np.asarray(%s)" % subdirectory)
        exec("np.savetxt('data/%s', npImage, delimiter=',')" % subdirectory)


def main():
    train()

if __name__ == '__main__':
    main()

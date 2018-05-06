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

def uploadDatabase(file):
    length = len( np.fromfile(file, float, -1 , ',') )
    matrix = np.loadtxt(file, usecols=range(length), dtype=float, delimiter=',')
    list = matrix.tolist()
    return (list)

def KNN(k ,element, classes, vectors):
    distances = []
    for categories in vectors:
        disAux = []
        for individuals in categories:
            sum = 0
            for i in range(len(individuals)):
                sum = sum + (element[i][0] - individuals[i])**2
            disAux.append(sum)
        distances.append(disAux)
    scores = []
    for i in range(len(vectors)):
        scores.append(0)
    while True:
        min = 1000
        for j in range(len(distances)):
            for k in range(len(distances[j])):
                if distances[j][k] < min:
                    min = distances[j][k]
                    rowmin = j
                    columnmin = k
        scores[rowmin] = scores[rowmin] + 1
        distances[rowmin][columnmin] = 1000
        if max(scores) == 3:
            break;
    print(scores)
    category = classes[scores.index(max(scores))]
    return category

def main():
    classes = []
    featuresMatrix = []
    for subdirectory in os.listdir("data"):
        directory = "data/" + subdirectory
        features = uploadDatabase(directory);
        classes.append(subdirectory)
        featuresMatrix.append(features)
    #imgName = input("Ingrese la imagen a clasificar:")
    imgName = "tuerca4.jpeg"
    image = cv2.imread(imgName, 0)
    if image is None:
        print("Image not found")
    else:
        print ("Image found")
        procImage = imageProcessing(image).tolist()
        k = 3
        imageClass = KNN(k, procImage, classes, featuresMatrix)
        print (imageClass)

if __name__ == '__main__':
    main()

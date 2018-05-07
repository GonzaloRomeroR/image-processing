import cv2
import numpy as np
import os
import imageProcessing as im

def uploadDatabase(file):
    matrix = np.load(file)
    list = matrix.tolist()
    # length = len( np.fromfile(file, float, -1 , ',') )
    # matrix = np.loadtxt(file, usecols=range(length), dtype=float, delimiter=',')
    return (list)

def KNN(k ,element, classes, vectors):
    distances = []
    for categories in vectors:
        disAux = []
        for individuals in categories:
            sum = 0
            for i in range(len(individuals)):
                sum = sum + (element[i][0] - individuals[i][0])**2
            disAux.append(sum)
        distances.append(disAux)
    scores = []
    for i in range(len(vectors)):
        scores.append(0)
    while True:
        min = 1000
        for j in range(len(distances)):
            for h in range(len(distances[j])):
                if distances[j][h] < min:
                    min = distances[j][h]
                    rowmin = j
                    columnmin = h
        scores[rowmin] = scores[rowmin] + 1
        distances[rowmin][columnmin] = 1000
        if max(scores) == k:
            break;
    #print ("The scores are:")
    #print(scores)
    category = classes[scores.index(max(scores))]
    return category

def classify(imgName):
    classes = []
    featuresMatrix = []
    for subdirectory in os.listdir("data"):
        directory = "data/" + subdirectory
        features = uploadDatabase(directory);
        name, extension = subdirectory.split('.')
        classes.append(name)
        featuresMatrix.append(features)
    #imgName = input("Ingrese la imagen a clasificar:")
    #imgName = "tuerca13.jpg"
    image = cv2.imread(imgName, 0)
    if image is None:
        pass
        #print("Image not found")
    else:
        #print ("Image found")
        procImage = im.imageProcessing(image).tolist()
        k = 3
        imageClass = KNN(k, procImage, classes, featuresMatrix)
        #print ("Image category: %s" % imageClass)
        return imageClass

def main():
    pass

if __name__ == '__main__':
    main()

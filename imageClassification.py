# Program to classify images, gets an image as an input and returns a category as output

import cv2
import numpy as np
import os
import imageProcessing as im

def uploadDatabase(file):
    # Load .npy used as database
    matrix = np.load(file)
    # Convert numpy matrix to list
    list = matrix.tolist()
    # length = len( np.fromfile(file, float, -1 , ',') )
    # matrix = np.loadtxt(file, usecols=range(length), dtype=float, delimiter=',')
    return (list)

def KNN(k ,element, classes, vectors):
    # Array to obtain distances to the node
    distances = []
    for categories in vectors:
        disAux = []
        for individuals in categories:
            sum = 0
            # Calculate distances
            for i in range(len(individuals)):
                sum = sum + (element[i][0] - individuals[i][0])**2
            disAux.append(sum)
        distances.append(disAux)
    # Array to get the scores of every class
    scores = []
    for i in range(len(vectors)):
        scores.append(0)
    while True:
        min = 1000
        for j in range(len(distances)):
            for h in range(len(distances[j])):
                if distances[j][h] < min:
                    # Get nodes with the shorter distances
                    min = distances[j][h]
                    rowmin = j
                    columnmin = h
        # Increse scores of the class which has a minimum
        scores[rowmin] = scores[rowmin] + 1
        distances[rowmin][columnmin] = 1000
        # In case that the maximum score reaches k, the clustering algorithm finishes
        if max(scores) == k:
            break;
    #print ("The scores are:")
    #print(scores)
    # Get category string
    category = classes[scores.index(max(scores))]
    return category

def classify(imgName):
    # Define class string array
    classes = []
    # Define calss feature matrix
    featuresMatrix = []
    for subdirectory in os.listdir("data"):
        directory = "data/" + subdirectory
        # Upload databases from .npy array
        features = uploadDatabase(directory);
        # Get name of class, splitting the string to get ride of ".npy" extension
        name, extension = subdirectory.split('.')
        # Define classes and their respective features vectors
        classes.append(name)
        featuresMatrix.append(features)
    #imgName = input("Ingrese la imagen a clasificar:")
    #imgName = "tuerca13.jpg"
    # Read image
    image = cv2.imread(imgName)
    if image is None:
        pass
        #print("Image not found")
    else:
        #print ("Image found")
        # Process the image to get a feature array
        procImage = im.imageProcessing(image).tolist()
        # Define KNN's k.
        k = 3
        # Class the image using KNN
        imageClass = KNN(k, procImage, classes, featuresMatrix)
        #print ("Image category: %s" % imageClass)
        # Return the category of the image
        return imageClass

def main():
    pass

if __name__ == '__main__':
    main()

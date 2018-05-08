# Program to test the algorithm performance

import os
import imageClassification as iC
def main():
    # List images in the training directory
    for directories in os.listdir("training"):
        # Sucess counter
        success = 0
        # Image counter
        numberImages = 0
        subdirectories = "training/" + directories
        for images in os.listdir(subdirectories):
            imagePath = subdirectories + '/' + images
            # Classify image
            category = iC.classify(imagePath)
            # Get if the classification was correct
            if category != None:
                # Increase the counter for every image read
                numberImages = numberImages + 1
            if category == directories:
                # In case it was correct increase the counter by one unit
                success = success + 1
        # Get success percentage
        successPercentage = float(success) / numberImages * 100
        print ("The percentage of success of " + directories + " = %s %%" % successPercentage)



if __name__ == '__main__':
    main()

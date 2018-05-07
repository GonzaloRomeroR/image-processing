import os
import imageClasification as iC
def main():
    for directories in os.listdir("training"):
        success = 0
        numberImages = 0
        subdirectories = "training/" + directories
        for images in os.listdir(subdirectories):
            imagePath = subdirectories + '/' + images
            category = iC.classify(imagePath)
            if category != None:
                numberImages = numberImages + 1
            if category == directories:
                success = success + 1
        successPercentage = float(success) / numberImages * 100
        print ("The percentage of success of " + directories + " = %s %%" % successPercentage)



if __name__ == '__main__':
    main()

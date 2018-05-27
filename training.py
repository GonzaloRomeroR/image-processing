# Train the algorithm

import cv2
import numpy as np
import os
import imageProcessing as im

def train():
    # List all images in the training directory
    for subdirectory in os.listdir("training"):
        exec("%s = []" % subdirectory)
        path = "training/" + subdirectory
        for j in range(len(os.listdir(path))):
            # Get image path
            imageName = subdirectory + str(j) + ".jpg"
            # Read the image using openCV
            image = cv2.imread(path + "/" + imageName)
            if image is None:
                print("Image " + subdirectory + str(j) + ".jpg" +" not found")
            else:
                print (subdirectory + str(j) + ".jpg" + " done")
                # Process the image: preprocessing and features extraction
                procImage = im.imageProcessing(image)
                # Append to features matrix
                exec("%s.append(procImage)" % subdirectory)
        # Create numpy array to save in .npy file
        exec("npImage = np.asarray(%s)" % subdirectory)
        # Save data in a .npy file
        exec("np.save('data/%s', npImage)" % subdirectory)
        #exec("np.savetxt('data/%s', npImage, delimiter=',')" % subdirectory)


def main():
    train()

if __name__ == '__main__':
    main()

import cv2
import numpy as np
import os
import imageProcessing as im


def train():
    for subdirectory in os.listdir("training"):
        exec("%s = []" % subdirectory)
        path = "training/" + subdirectory
        for j in range(len(os.listdir(path))):

            imageName = subdirectory + str(j) + ".jpg"
            image = cv2.imread(path + "/" + imageName, 0)
            if image is None:
                print("Image " + subdirectory + str(j) + ".jpg" +" not found")
            else:
                print (subdirectory + str(j) + ".jpg" + " done")
                procImage = im.imageProcessing(image)
                exec("%s.append(procImage)" % subdirectory)
        exec("npImage = np.asarray(%s)" % subdirectory)
        exec("np.save('data/%s', npImage)" % subdirectory)
        #exec("np.savetxt('data/%s', npImage, delimiter=',')" % subdirectory)


def main():
    train()

if __name__ == '__main__':
    main()

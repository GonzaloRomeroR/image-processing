# Example of a single image classification

import imageClassification as iC

def main():
    # Classify image, the output is the category of the image
    category = iC.classify("training/tornillo/tornillo0.jpg")
    print (category)

if __name__ == '__main__':
    main()

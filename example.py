import imageClasification as iC

def main():
    category = iC.classify("training/tornillo/tornillo0.jpg")
    print (category)

if __name__ == '__main__':
    main()

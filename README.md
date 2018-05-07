# Image classification using OpenCV
## Usage:

###Training
Need to save images in the training folder, then run the training file to obtain a feature database.

`python3 training.py`

###Testing
To test the performance of the training run test.py, its output will show the percentage of success.

`python3 test.py`

###Clasification
To classify an image run the following code.
```
import imageClasification as iC
category = iC.classify("path/to/image")

```

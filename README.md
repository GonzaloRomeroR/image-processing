# Image classification using OpenCV
## Usage:

### Training
Need to save images in the training folder in the same way as in the given example, then run the training.py file to obtain a feature database.

`python3 training.py`

### Testing

To test the performance of the training algorithm run test.py, its output will show the percentage of success for every defined class.

`python3 test.py`

### Clasification

To classify an image run the following code.
```
import imageClasification as iC
category = iC.classify("path/to/image")

```

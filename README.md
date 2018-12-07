# Navigation for the blind
An algorithm that detects and outlines sidewalks or driving lanes using python. These outlines can be used to help the blind navigate. The programs gives real time voice feed backs to the blind. \
P.S - This algorithm was originally made to detect sidewalks. It just happened to work on driving lanes too.
## Getting started
Both the python files have to be ran simultaneously. The detection.py file will append it's results into a text file. The output.py file will read the results and say it out loud for the blind.
### Prerequisites
* Opencv (image processing module)
* Numpy (support for large multi-dimensional arrays and matrices)
* Math
* Time
* Scipy (polynomial regression)
* pyttsx3 (text to speech)
### Installation
All the wheel files for python 3 can be downloaded from https://www.lfd.uci.edu/~gohlke/pythonlibs/
To install, run

    pip install WheelFileName.whl

Alternative - 

    pip install opencv-python
    pip install numpy
    pip install pyttsx3
    pip install scipy
## Running the algorithm
Both the files detection.py and out.py have to be run simultaneously. The file detection.py is running its algorithm over a mp4 video called challenge.mp4. However, the same algorithm can be performed over a live video feed from a camera.
## How it works
The algorithm uses the results from hough lines probabilistic (an opencv algorithm) and creates 2 linear lines to outline driving lanes. Experiments suggests that the 2 linear lines will intersect if the driving lanes curve or turn. \

Perform edge detection over the frames from challenge.mp4 \
![GitHub Logo](/Results/edgeDetection.jpg)

Cut out reigon of interest. \
![GitHub Logo](/Results/ROI.jpg)

Perform hough lines probabilistic over ROI frames. \
![GitHub Logo](/Results/houghLines.jpg)

Average out 2 linear lines using the results from hough lines probabilistic. \
![GitHub Logo](/Results/linearLines.jpg)

Perform quadratic regression on hough line results to outline the lanes. \
![GitHub Logo](/Results/polyReg.jpg)

Final results - \
![GitHub Logo](/Results/detections.jpg)

## Built with
* Python3
* A ton of pizza at a hackathon ;)




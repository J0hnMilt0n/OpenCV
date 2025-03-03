#Basics
"""
Reading Images and Video
Image Transformations 
Drawing Shapes
Including Text
"""
#Advanced
"""
Switching Between Color Spaces
Biwise operations
Masking
Histogram Computation
Edge Detection
Face Recognition, Hand Detection
Deep Computer Vision (Characters Identification)
"""
#pip install opencv-contrib-python
#pip install caer
import cv2 as cv

#Read and Display Images
'''
#Read Image
img = cv.imread('images/cat.png') #for large we need to resize/rescale the frame size

# Display Image
cv.imshow('Cat', img)

# Wait for Key Press
cv.waitKey(0)
'''
#Capturing Video and Displaying
'''capture = cv.VideoCapture('videos/cat_video.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
cv.waitKey(10)'''

#Resizing Rescaling 

'''def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('videos/cat_video.mp4')
while True:
    isTrue, frame = capture.read()
    frame = rescaleFrame(frame)
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
cv.waitKey(10)'''

#only for live stream
'''def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture(0)
# changeRes(30,50)
while True:
    isTrue, frame = capture.read()
    cv.imshow('video',frame)
    if cv.waitKey(20) & 0xff==ord('e'):
        break'''






import cv2 as cv
import numpy as np
import random

# define a video capture object 
vid = cv.VideoCapture(0) 

#colors written in BGR format
red = (0, 0, 255)
orange = (0, 128, 255)
yellow = (0, 255, 255)
purple = (255, 0, 128)
blue = (255, 0, 0)
green = (0, 255, 0)


while(True): 

    # Capture the video frame 
    # by frame 
    ret, frame = vid.read()

    left_corner = (random.randint(0, 100),  random.randint(0, 100))
    right_corner = (random.randint(120, 600),  random.randint(130, 600))

    frame = cv.rectangle(frame, left_corner, right_corner, green, 10)

    # Display the resulting frame 
    cv.imshow('Frames', frame)

    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv.destroyAllWindows() 


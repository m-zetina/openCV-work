import cv2
import numpy as np
import random

rectangle_points = []
drawing = False

# define a video capture object 
vid = cv2.VideoCapture(0) 

#colors written in BGR format
red = (0, 0, 255)
orange = (0, 128, 255)
yellow = (0, 255, 255)
purple = (255, 0, 128)
blue = (255, 0, 0)
green = (0, 255, 0)

def redraw_rectangle(event, x, y, flags, param):
    global rectangle_points, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        rectangle_points = [(x, y)]
        drawing = True
    
    elif event == cv2.EVENT_LBUTTONUP:
        rectangle_points.append((x, y))
        drawing = False

while(True): 

    # Capture the video frame 
    # by frame 
    ret, frame = vid.read()
    if ret:

        try:
            frame = cv2.rectangle(frame, rectangle_points[0], rectangle_points[1], green, 2)
        except:
            pass

        # Display the resulting frame 
        cv2.imshow('Frames', frame)
        cv2.setMouseCallback('Frames', redraw_rectangle)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('r'):
            rectangle_points = []

        # the 'q' button is set as the 
        # quitting button you may use any 
        # desired button of your choice 
        if key == ord('q'):
            break
        
        if len(rectangle_points) == 2:
            rectangle_coords = f'pt1: {rectangle_points[0]}, pt2: {rectangle_points[1]}'
            print(rectangle_coords)

# After the loop release the cap object 
vid.release()
# Destroy all the windows 
cv2.destroyAllWindows() 


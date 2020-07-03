import cv2
import numpy as np
import random

pixel_point = []
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

# def draw_points(event, x, y, flags, param):
#     global pixel_point, drawing

#     if event == cv2.EVENT_RBUTTONDBLCLK: drawing = not(drawing)
#     if drawing:
#         if cv2.EVENT_LBUTTONDOWN:
#             pixel_point.append((x, y))
#     else:
#         if cv2.EVENT_LBUTTONDOWN:
#             try: 
#                 pixel_point.remove((x, y))
#             except:
#                 pass

def draw_points(event, x, y, flags, param):
    global pixel_point, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pixel_point.append((x, y))


while(True): 

    # Capture the video frame 
    # by frame 
    ret, frame = vid.read()
    if ret:

        try:
            for i in len(pixel_point):
                frame = cv2.rectangle(frame, pixel_point[i], (pixel_point[i][0]+5, pixel_point[i][1]+5), green, -1)
        except:
            pass

        # Display the resulting frame 
        cv2.imshow('Frames', frame)
        cv2.setMouseCallback('Frames', draw_points)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('r'):
            pixel_point = []

        if key == ord('q'):
            break
        
        if len(pixel_point) > 0:
            print(pixel_point)
            
# After the loop release the cap object 
vid.release()
# Destroy all the windows 
cv2.destroyAllWindows() 


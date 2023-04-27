# video/camera to text
Convert camera captured or video file into plain text on terminal using openCV, numpy and Pillow(to display the result in seperate windows).
## How it work
The program will convert the input to grey format frame by frame and mask the value in each pixel from 0-255 into 0-9, which the value will represent the proper character in that pixel, then making an array by substituting the value with characters by its order to make a plain text output frame by frame.

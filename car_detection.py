import cv2

#capture the frame from a video
cap = cv2.VideoCapture("video.avi")

#trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier("cars.xml")

# loop run if capturing has been initialised.
while True:
    #read frame from a video
    ret, frames = cap.read()

    #convert to gray scales of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    #detect cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray,1.1, 1)

    #to draw a rectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('video2', frames)
                
    #wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
# Программа дял выделения контуров с элементом управления
import cv2
image = cv2.imread('2.jpeg')
cv2.namedWindow('Edged')
def nothing(x):
    pass
cv2.createTrackbar("Lower",'Edges',0,255, nothing)
cv2.createTrackbar("Upper",'Edges',0,255, nothing)

while True:
    lower_trash = cv2.getTrackbarPos("Lower",'Edges')
    upper_trash = cv2.getTrackbarPos("Upper",'Edges')
    edges = cv2. Canny(image,lower_trash,upper_trash)
    cv2.imshow('Edges',edges)

    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()  
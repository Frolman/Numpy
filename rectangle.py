# Программа для добавления прямоугольника на изображение
import cv2

image = cv2.imread('2.jpeg')

cv2.rectangle(image,(100,100), (300,500), (0,255,0),3)
cv2.imshow('Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
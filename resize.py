# Программа для изменения изображений
# начальные размеры 2001х1122
import cv2

image = cv2.imread('new_1.jpeg')

#Изменение размера
resize_image = cv2.resize(image,(1000,800))
cv2.imshow ('Resize Image', resize_image)
cv2.imwrite ('2.jpeg', resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows

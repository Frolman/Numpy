# Программа для размытия изображения
import cv2

image = cv2.imread("2.jpeg")

blurred_image = cv2.GaussianBlur(image, (55, 15), 0)

cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
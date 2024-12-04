# Программа для создания черно-белого изображения
import  cv2

image = cv2.imread('2.jpeg')

grey_image = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)

cv2.imshow ("Grey image", grey_image)
cv2.imwrite('grey.jpeg', grey_image )
cv2.waitKey(0)
cv2.destroyAllWindows
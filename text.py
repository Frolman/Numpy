#Программа для добавления текста на изображение
import cv2

image = cv2.imread ('2.jpeg')
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
text = "FROLMAN"
cv2.putText(image, text, (400,300), font, 2,(0,0,0),2)
cv2.imshow ("Text in image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
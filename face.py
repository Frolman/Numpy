#Программа для распознавания лица
#Подключение билиотеки opecv
import cv2

#Загрузка каскада
cascad_src = 'haarcascade_frontalface_default.xml'
face_cascad = cv2.CascadeClassifier(cascad_src)

#Загрузка изображений
image = cv2.imread ('face_1.jpq')

#Перевод в градации серого
grey_image = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)

#Обнаружение лиц на изображении
faces = face_cascad.detectMultiScale(gray, csaleFactor=1.1, minNeighbors=2,minSize = (100,100))

#Выделение распознанных областей
for (x,y,w,h) in faces:
    cv2.rectangle(x,y,(x+w,y+h,(0,0,255),4))

#Отображение результатов
cv2.imshow("Detected Faces",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
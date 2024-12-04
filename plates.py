#Программа для распознавания лица
#Подключение билиотеки opecv
import cv2

#Загрузка каскада
cascad_src = 'haarcascade_russian_plate_number.xml'
face_cascad = cv2.CascadeClassifier(cascad_src)

#Загрузка изображений
image = cv2.imread ('car_2.jpg')

#Перевод в градации серого
grey_image = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)

#Обнаружение лиц на изображении
faces = face_cascad.detectMultiScale(grey_image, scaleFactor=1.01, minNeighbors=2,minSize = (20,20))

#Выделение распознанных областей
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

#Отображение результатов
cv2.imshow("Detected Faces",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
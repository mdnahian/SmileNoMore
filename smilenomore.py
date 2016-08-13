import cv2

mc = cv2.CascadeClassifier("Mouth.xml")
image = cv2.imread("img/sadface.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

mouths = mc.detectMultiScale(
		gray,
		scaleFactor = 1.1,
		minNeighbors = 5,
		minSize = (100, 20),
		flags = cv2.CASCADE_SCALE_IMAGE
)

for (x, y, w, h) in mouths:
	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite("img/newsad.jpg", image)

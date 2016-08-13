import os
import cv2
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'img/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/upload', methods=['POST'])
def upload():
	file = request.files['file']
	if file and allowed_file(file.filename):
		filename = file.filename
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		
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

		return redirect(url_for('uploaded_file', filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
	app.run(
		host="0.0.0.0",
		port=int("80"),
		debug=True
	)

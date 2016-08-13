import os
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

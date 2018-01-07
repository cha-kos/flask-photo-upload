import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from pdb import set_trace as bp

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route('/')

def index():
    return render_template('upload.html')

if __name__ == "__main__":
    app.run()

@app.route('/upload', methods=['POST'])
def upload():
    imageFile = request.files['file']

    # encode image to base64 so we can place directly inline inside html <img/>
    image = imageFile.read().encode('base64').replace('\n', '')
    return render_template("display.html", image = image)

if __name__ == "__main__":
    app.run(port=4555, debug=True)

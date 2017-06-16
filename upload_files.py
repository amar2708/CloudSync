from flask import Flask, render_template, request, send_file
import os
import urllib
from crud_app import insert

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '/tmp'
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg','gif'])

path = "tmp/"

@app.route('/')
def home():
    return "this is a home page..."

@app.route('/upload_images', methods=['POST'])
def upload():
    files = request.files['img_name']
    files.save(os.path.join(app.config['UPLOAD_FOLDER'], "house.png"))
    insert("house.png")
    return "files uploaded successfully"

@app.route('/download_images', methods=['GET'])
def download():
    files = request.args.get('img_name')
    print(files)
    return send_file("/"+path+files, mimetype='image/png')
    
@app.route('/delete_images', methods=['DELETE'])
def delete():
    files = request.args.get('img_name')
    os.remove("/"+path+files)
    return "files deleted successfully..."


if __name__ == "__main__":
    app.run(debug = True)

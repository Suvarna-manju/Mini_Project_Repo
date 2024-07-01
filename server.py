from flask import Flask,request,jsonify
import os
from werkzeug.utils import secure_filename
app=Flask(__name__)
UPLOAD_FOLDER='uploads'
ALLOWED_EXTENSIONS={'jpg','jpeg','gif','png','pdf'}
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
def allow_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'Error':'No File Part!!!'})
    file = request.files['file']
    if file.filename=='':
            return jsonify({'Error':'No Selected File!!!'})
    if file and allow_file(file.filename):
        filename =secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return jsonify({'Success':'File Is Successed Plz Try Again Once !!!'})
    else:
        return jsonify({'Error':'File Is Not Found,Plz Try Again Once !!!' })
if __name__ =='__main__':
    os.makedirs(UPLOAD_FOLDER,exist_ok=True)
    app.run(debug=True)
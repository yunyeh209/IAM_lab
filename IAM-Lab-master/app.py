from flask import Flask, render_template, request
from flask_cors import CORS
import boto3

app = Flask(__name__)
CORS(app)

s3_client = boto3.client('s3')

BUCKET_NAME = '<your bucket name>'

# @app.route('/')
# def home():
#     return render_template("index.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        fileName = img.filename
        fileExtension = fileName.split('.')[1]
        if (fileExtension in ['jpg', 'jpeg', 'JPG', 'JPEG', 'PNG', 'png']):
            s3_client.put_object(
                Body = img, 
                Bucket = BUCKET_NAME, 
                Key = fileName, 
                ContentType = 'image/'+fileExtension)
            msg = "Upload done !"
        else:
            msg = "Error file type !"
    return msg
    return render_template("index.html", msg = msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

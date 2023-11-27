from flask import Flask, render_template, request, redirect
import boto3
import os

app = Flask(__name__)

# Set your AWS credentials and S3 bucket name
AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
S3_BUCKET_NAME = 'S3_BUCKET_NAME'

# Configure the S3 client
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        # Upload the file to S3
        s3.upload_fileobj(file, S3_BUCKET_NAME, file.filename)
        return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)

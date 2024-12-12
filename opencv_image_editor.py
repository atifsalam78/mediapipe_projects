from flask import Flask, render_template, request, flash, redirect, url_for, Response
from werkzeug.utils import secure_filename
import numpy as np
import cv2 as cv
import os
# import contextlib
# from contextlib import ExitStack


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg', 'gif'}

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def frame_generator():
    camera = cv.VideoCapture(0)
    
    
    while True:
        
        sucess, frame = camera.read()
        if not sucess:
                break
        else:
            detector = cv.CascadeClassifier("D:/mediapipe_projects/hand_gesture/models/haarcascade_frontalface_default.xml")
            # eye_cascade = cv.CascadeClassifier("D:/mediapipe_projects/hand_gesture/models/haarcascade_eye.xml")
            faces = detector.detectMultiScale(frame, 1.1,7)
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            
            # Draw rectangle
            for (x, y, w, h) in faces:
                cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                roi_gray = gray[y: y+h, x: x+w]
                # roi_color = frame[y: y+h, x: x+w]
                # eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
                # for (ex, ey, ew, eh) in eyes:
                #     cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)  
            
            ret, buffer = cv.imencode(".jpg", frame)
            frame = buffer.tobytes()
        
            
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    camera.release()
    cv.destroyAllWindows()
    # with ExitStack() as stack:
    #     stack.callback(camera.release)
    #     stack.callback(cv.destroyAllWindows)
        

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(filename, operation):
    print("The operation is {} and file name is {}".format(operation, filename))
    img = cv.imread("uploads/{}".format(filename))
    match operation:
        case "cgray":
            imgProcessed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            NewFilename = "static/{}".format(filename)
            cv.imwrite(NewFilename, imgProcessed)
            return NewFilename
        case "cpng":
            NewFilename = "static/{}.png".format(filename.split('.')[0])
            cv.imwrite(NewFilename, img)
            return NewFilename
        
        case "cwebp":
            NewFilename = "static/{}.webp".format(filename.split('.')[0])
            cv.imwrite(NewFilename, img)
            return NewFilename
        case "cjpg":
            NewFilename = "static/{}.jpg".format(filename.split('.')[0])
            cv.imwrite(NewFilename, img)
            return NewFilename
        case "cbitnot":
            imgProcessed = cv.bitwise_not(img)
            NewFilename = "static/{}".format(filename)
            cv.imwrite(NewFilename, imgProcessed)
            return NewFilename

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        operation = request.form.get("operation")
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "error: No selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new = process_image(filename, operation)
            flash("Your image has been processed and available <a href='/{}' target='blank'>here</a>".format(new))
            return render_template("index.html")
    return render_template("index.html")

@app.route("/stream")
def stream():
    return render_template("new.html")

@app.route("/video")
def video():    
    return Response(frame_generator(),mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__=="__main__":
    app.run(debug=True)

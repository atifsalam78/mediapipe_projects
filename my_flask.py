from flask import Flask

# WSGI Application

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome my new web page developed in Python Flask"

@app.route("/contact")
def contact():
    return "You may contact with us any time you want 24/7"

@app.route("/about")
def about():
    return "Hew you know more about us"

if __name__=="__main__":
    app.run(debug=True)


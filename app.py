# Importing required libs
from flask import Flask, render_template, request
app = Flask(__name__)

# Home route
@app.route("/")
def main():
    return render_template("index.html")

# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    return render_template("result.html")
# Importing required libs
from flask import Flask, render_template, request
from model import preprocess_img, predict_results
 
# Instantiating flask app
app = Flask(__name__)
 
 
# Home route
@app.route("/")
def main():
    return render_template("index.html")
 
 
# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    try:
        if request.method == 'POST':
            img = preprocess_img(request.files['file'].stream)
            prediction, other_classes = predict_results(img)
            
            labels = [row[0].replace('_',' ').title() for row in other_classes] 
            labels.append('Other')           
            for row in other_classes:
                print(row)

            values = [round(row[1],2) for row in other_classes]
            other_value = 100 - sum(values)
            values.append(other_value)

            return render_template("result.html", prediction=str(prediction), labels=labels,values=values)
 
    except:
        if request.files['file'].filename == '':
            error = "No file selected."
        else:    
            error = "File cannot be processed."
        return render_template("result.html", error=error)
 
 
# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
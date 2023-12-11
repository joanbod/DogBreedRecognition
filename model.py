# Importing required libs
from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from PIL import Image
import pandas as pd
 
# Loading model

model = load_model('path')
 
# Preparing and pre-processing the image
def preprocess_img(img_path):
    op_img = Image.open(img_path)
    img_resize = op_img.resize((256, 256))
    img2arr = img_to_array(img_resize) / 255.0
    img_reshape = img2arr.reshape(1, 256, 256, 3)
    return img_reshape
 
 
# Predicting function
def predict_results(predict_img_array):
    # Load the class mapping from CSV
    csv_file_path = "path"  
    df = pd.read_csv(csv_file_path) 
    predictions = model.predict(predict_img_array)

    # Get the index of the predicted class
    predicted_class_index = np.argmax(predictions)

    # Get the corresponding class label and format it displayed form
    predicted_class = df.iloc[predicted_class_index, 0].replace('_',' ').title()

    # Get the probability/confidence score for the predicted class
    confidence_score = predictions[0][predicted_class_index]

    #If less than 5% confidence score then do not show these classes
    threshold_percentage = 5
    other_classes = [(df.iloc[i, 0], predictions[0][i] * 100) for i in range(len(predictions[0])) if predictions[0][i] >= threshold_percentage / 100]
    # Sort other_classes by values in the second column (confidence scores) in descending order
    sorted_other_classes = sorted(other_classes, key=lambda x: x[1], reverse=True)


    return predicted_class, sorted_other_classes
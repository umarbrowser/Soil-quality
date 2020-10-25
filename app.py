
from flask import Flask, request, render_template #import main Flask class and request object
"""from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from werkzeug.utils import secure_filename

import os, sys, glob, re"""

app = Flask(__name__) #create the Flask app
app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
)
"""model_path = "model.h5"

SoilNet = load_model(model_path)

classes = {0:"Alluvial Soil can produce ( Rice,Wheat,Sugarcane,Maize,Cotton,Soyabean,Jute )",1:"Regular Soil can produce ( Virginia, Wheat , Jowar,Millets,Linseed,Castor,Sunflower) ",2:"Clay Soil can produce ( Rice,Lettuce,Chard,Broccoli,Cabbage,Snap Beans )",3:"Laterite soil can produce (Cotton,Wheat,Pilses,Millets,OilSeeds,Potatoes )"}

def model_predict(image_path,model):Regur Soil
    print("Predicted")
    image = load_img(image_path,target_size=(150,150))
    image = img_to_array(image)
    image = image/255
    image = np.expand_dims(image,axis=0)
    
    result = np.argmax(model.predict(image))
    prediction = classes[result]
    
    
    if result == 0:
        print("Alluvial_soil.html")
        
        return "Alluvial","Alluvial_soil.html"
    elif result == 1:
        print("Regular_soil.html")
        
        return "Regular Soil", "Regular_soil.html"
    elif result == 2:
        print("Clay_soil.html")
        
        return "Clay Soil" , "Clay_soil.html"
    elif result == 3:
        print("Laterite_soil.html")
        
        return "Laterite Soil" , "Laterite_soil.html"
        """


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('/index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    return render_template('Alluvial_soil.html')
'''
    print("Entered")
    if request.method == 'POST':
        print("Entered here")
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = M.model_predict(file_path,SoilNet)
        return render_template(output_page, pred_output = pred, user_image = file_path)
'''
             
        

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000


from flask import Flask, request, render_template #import main Flask class and request object
import model_predict as M

app = Flask(__name__) #create the Flask app

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('/index.html')
'''
@app.route('/predict',methods=['GET','POST'])
def predict():
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
              
        return render_template(output_page, pred_output = pred, user_image = file_path)'''


if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000

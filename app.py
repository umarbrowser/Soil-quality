from flask import Flask, request, render_template
##from model_predict import model_predict
app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

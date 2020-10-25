from flask import Flask, request, render_template
import model_predict from model_predict
app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

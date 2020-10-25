
from flask import Flask, request, render_template #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')


if _name == '__main_':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000

import os
from flask import Flask, render_template

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    APP_PATH = os.path.dirname(__file__)


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('/index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

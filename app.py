from flask import Flask, render_template
# from pymongo import MongoClient

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg='Flask is Cool!!')


if __name__ == '__main__':
    app.run(debug=True) 
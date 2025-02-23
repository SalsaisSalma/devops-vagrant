from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # link to /about page
    return '<p>Hello, World! <a href="/about">About</a></p>'

@app.route('/about')
def about():
    return '<p>This is a Flask web app running in a Linux VM.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0') 

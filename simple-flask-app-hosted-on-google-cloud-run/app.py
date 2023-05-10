
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page, my guy!'

@app.route('/second-route')
def second_route():
    return 'This is the second route.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hello World Class Developers'
    return render_template('index.html')

@app.route('/whereami')
def whereami():
    return'I am in Ghana'

if __name__ == '__main__' :
    app.run(debug=True, host='0.0.0.0')
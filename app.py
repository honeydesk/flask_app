from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/predict')
def predict():
    return 'kya be!'

if __name__ == "__main__":
    app.run(debug=True)
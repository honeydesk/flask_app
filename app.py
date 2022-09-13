from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return render_template('index.html')
    
@app.route('/predict')
def predict():
    return 'kya be!'

if __name__ == "__main__":
    app.run(debug=True)
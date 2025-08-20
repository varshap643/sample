from flask import Flask
app = Flask(__name__)
@app.route('/') 
def firstApp():
    return "Hello World"
    return "This is devops lab"
app.run(debug=True)

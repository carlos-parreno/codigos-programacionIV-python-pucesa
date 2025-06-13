from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a Flask, soy Carlos"

@app.route('/templates/base.html')
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug = True)
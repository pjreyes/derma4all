from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/cart')

def cart():
    return render_template('cart.html')
if __name__ == '__main__':
    app.run(host="192.168.1.104",debug=True)
from flask import Flask, render_template
import requests, os
app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/cart')

def cart():
    return render_template('cart.html')
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port,debug=True)
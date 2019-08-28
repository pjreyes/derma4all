from flask import Flask, render_template
import requests, os
app = Flask(__name__)

@app.route('/')

def home():
    productos = [
        {'brand': 'Klapp', 'text': 'Cremas para distintos tipos de uso, siempre pensando en tu cuidado y belleza','name':'klap_products'},
        {'brand': 'DermaPen', 'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vel metus nec mi ornare posuere.','name':'needles_dermapen'},
        {'brand': 'PlasmaPen', 'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vel metus nec mi ornare posuere.','name':'needles_plasmapen'}
    ] # este array debe ser un servicio con BD

    return render_template('index.html', productos=productos)

@app.route('/cart')

def cart():
    return render_template('cart.html')
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port,debug=True)
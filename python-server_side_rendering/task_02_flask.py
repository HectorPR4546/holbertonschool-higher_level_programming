from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    try:
        with open('products.json', 'r') as f:
            products_data = json.load(f)
    except FileNotFoundError:
        products_data = []
    return render_template('products.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

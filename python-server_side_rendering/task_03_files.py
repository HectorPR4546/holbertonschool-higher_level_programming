from flask import Flask, render_template, request
import json
import csv

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

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except FileNotFoundError:
        items_list = []
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products_data = []
    error_message = None

    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products_data = json.load(f)
        except FileNotFoundError:
            error_message = "products.json not found."
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    products_data.append({
                        "id": int(row['id']),
                        "name": row['name'],
                        "category": row['category'],
                        "price": float(row['price'])
                    })
        except FileNotFoundError:
            error_message = "products.csv not found."
    else:
        error_message = "Wrong source. Please use 'json' or 'csv'."

    if product_id:
        filtered_products = [p for p in products_data if p['id'] == product_id]
        if not filtered_products:
            error_message = "Product not found."
        products_data = filtered_products

    return render_template('product_display.html', products=products_data, error=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

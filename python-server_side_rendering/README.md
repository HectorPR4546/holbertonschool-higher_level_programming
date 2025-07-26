# 0x00. Server-side rendering

This project focuses on understanding and implementing server-side rendering (SSR) using Python and Flask. It covers concepts like templating with Jinja2, handling dynamic content, and integrating data from various sources such as JSON, CSV, and SQLite databases.

## Task 0: Creating a Simple Templating Program

This task involves creating a Python function `generate_invitations` that generates personalized invitation files from a template and a list of attendee objects. It also includes robust error handling for various edge cases.

### How to Use

1.  **Save the template:** Create a file named `template.txt` with the following content:

    ```
    Hello {name},

    You are invited to the {event_title} on {event_date} at {event_location}.

    We look forward to your presence.

    Best regards,
    Event Team
    ```

2.  **Save the Python script:** Create a file named `task_00_intro.py` with the `generate_invitations` function.

3.  **Run the main script:** Create a `main.py` file to test the function:

    ```python
    # Main file content
    from task_00_intro import generate_invitations

    # Read the template from a file
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
    ```

    Execute `python3 main.py` in the same directory.

### Error Handling

The `generate_invitations` function handles the following error conditions:

-   **Invalid Input Types:** Checks if `template` is a string and `attendees` is a list of dictionaries. Logs an error and terminates if types are incorrect.
-   **Empty Template:** Logs an error message and terminates if the template string is empty.
-   **Empty List of Objects:** Logs an error message and terminates if the `attendees` list is empty.
-   **Missing Data in Object:** Replaces missing data for placeholders with "N/A" in the output file.

### Output

Upon successful execution, the script will generate `output_X.txt` files (e.g., `output_1.txt`, `output_2.txt`), each containing a personalized invitation.

## Task 1: Creating a Basic HTML Template in Flask

This task involves setting up a basic Flask application to serve HTML pages using Jinja templates. It demonstrates how to create a simple HTML template with various elements and how to render it using Flask. Additionally, it covers creating reusable header and footer templates for consistent layout across multiple pages.

### How to Use

1.  **Install Flask:** If you haven't already, install Flask:

    ```bash
    pip install Flask
    ```

2.  **Create the Flask application:** Create a Python file named `task_01_jinja.py` with the following content:

    ```python
    from flask import Flask, render_template

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

    if __name__ == '__main__':
        app.run(debug=True, port=5000)
    ```

3.  **Create the `templates` directory:** Inside your project directory, create a folder named `templates`.

4.  **Create HTML templates:** Inside the `templates` folder, create the following files:

    -   `index.html`:

        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Home</title>
        </head>
        <body>
            {% include 'header.html' %}
            <h1>Welcome to My Flask App</h1>
            <p>This is a simple Flask application.</p>
            <ul>
                <li>Flask</li>
                <li>HTML</li>
                <li>Templates</li>
            </ul>
            {% include 'footer.html' %}
        </body>
        </html>
        ```

    -   `header.html`:

        ```html
        <header>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </nav>
            <h1>My Flask App</h1>
        </header>
        ```

    -   `footer.html`:

        ```html
        <footer>
            <p>&copy; 2024 My Flask App</p>
        </footer>
        ```

    -   `about.html`:

        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>About</title>
        </head>
        <body>
            {% include 'header.html' %}
            <h1>About Us</h1>
            <p>This is the about page for our Flask application.</p>
            {% include 'footer.html' %}
        </body>
        </html>
        ```

    -   `contact.html`:

        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contact</title>
        </head>
        <body>
            {% include 'header.html' %}
            <h1>Contact Us</h1>
            <p>You can reach us at contact@example.com.</p>
            {% include 'footer.html' %}
        </body>
        </html>
        ```

5.  **Run the Flask application:** Execute `python3 task_01_jinja.py` in your terminal. Then, open your web browser and navigate to `http://127.0.0.1:5000/` to see the application in action.

## Task 2: Creating a Dynamic Template with Loops and Conditions in Flask

This task enhances the Flask application by integrating dynamic content into HTML templates using Jinja’s loop and conditional constructs. It involves reading a list of items from a JSON file and displaying them dynamically on a web page.

### How to Use

1.  **Prepare `items.json`:** Create a file named `items.json` in the project directory with the following content:

    ```json
    {
        "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
    }
    ```

2.  **Create `items.html` template:** In the `templates` folder, create `items.html`:

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Items List</title>
    </head>
    <body>
        {% include 'header.html' %}
        <h1>Items List</h1>
        {% if items %}
            <ul>
                {% for item in items %}
                    <li>{{ item }}</li>
                {% endfor %}
            </ul>
        {% else %}
            <p>No items found.</p>
        {% endif %}
        {% include 'footer.html' %}
    </body>
    </html>
    ```

3.  **Create `task_02_logic.py`:** Create a Python file named `task_02_logic.py` with the Flask application and the new `/items` route:

    ```python
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

    @app.route('/items')
    def items():
        try:
            with open('items.json', 'r') as f:
                data = json.load(f)
                items_list = data.get('items', [])
        except FileNotFoundError:
            items_list = []
        return render_template('items.html', items=items_list)

    if __name__ == '__main__':
        app.run(debug=True, port=5000)
    ```

4.  **Run the Flask application:** Execute `python3 task_02_logic.py` and navigate to `http://127.0.0.1:5000/items`.

## Task 3: Displaying Data from JSON or CSV Files in Flask

This task adds functionality to read and display product data from JSON and CSV files, allowing users to choose the data source via a query parameter. It also includes filtering by an optional `id` and handling edge cases.

### How to Use

1.  **Prepare Data Files:**

    -   `products.json` (already created in Task 0, but ensure it has the correct format):

        ```json
        [
            {
                "id": 1,
                "name": "Laptop",
                "category": "Electronics",
                "price": 1200.00
            },
            {
                "id": 2,
                "name": "Mouse",
                "category": "Electronics",
                "price": 25.00
            },
            {
                "id": 3,
                "name": "Keyboard",
                "category": "Electronics",
                "price": 75.00
            },
            {
                "id": 4,
                "name": "Monitor",
                "category": "Electronics",
                "price": 300.00
            },
            {
                "id": 5,
                "name": "Desk Chair",
                "category": "Furniture",
                "price": 150.00
            }
        ]
        ```

    -   `products.csv`:

        ```csv
        id,name,category,price
        1,Laptop,Electronics,799.99
        2,Coffee Mug,Home Goods,15.99
        ```

2.  **Create `product_display.html` template:** In the `templates` folder, create `product_display.html`:

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Product Display</title>
    </head>
    <body>
        {% include 'header.html' %}
        <h1>Product Information</h1>

        {% if error %}
            <p style="color: red;">{{ error }}</p>
        {% elif products %}
            <table border="1">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Category</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    {% for product in products %}
                        <tr>
                            <td>{{ product.name }}</td>
                            <td>{{ product.category }}</td>
                            <td>{{ product.price }}</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        {% else %}
            <p>No products to display.</p>
        {% endif %}
        {% include 'footer.html' %}
    </body>
    </html>
    ```

3.  **Create `task_03_files.py`:** Create a Python file named `task_03_files.py` with the Flask application and the new `/products` route:

    ```python
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
    ```

4.  **Run the Flask application:** Execute `python3 task_03_files.py` and navigate to `http://127.0.0.1:5000/products?source=json` or `http://127.0.0.1:5000/products?source=csv`.

## Task 4: Extending Dynamic Data Display to Include SQLite in Flask

This task adds the functionality to fetch and display data from a SQLite database in the Flask application. The application allows users to choose between JSON, CSV, and SQL (SQLite database) as data sources using the `source` query parameter.

### How to Use

1.  **Create `create_db.py`:** Create a Python file named `create_db.py` to set up and populate the SQLite database:

    ```python
    import sqlite3

    def create_database():
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
        conn.commit()
        conn.close()

    if __name__ == '__main__':
        create_database()
    ```

2.  **Run `create_db.py`:** Execute `python3 create_db.py` to create the `products.db` file.

3.  **Create `task_04_db.py`:** Create a Python file named `task_04_db.py` with the Flask application and the updated `/products` route to handle the `sql` source:

    ```python
    from flask import Flask, render_template, request
    import json
    import csv
    import sqlite3

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
        elif source == 'sql':
            try:
                conn = sqlite3.connect('products.db')
                cursor = conn.cursor()
                cursor.execute("SELECT id, name, category, price FROM Products")
                rows = cursor.fetchall()
                for row in rows:
                    products_data.append({
                        "id": row[0],
                        "name": row[1],
                        "category": row[2],
                        "price": row[3]
                    })
            except sqlite3.Error as e:
                error_message = f"Database error: {e}"
            finally:
                if conn:
                    conn.close()
        else:
            error_message = "Wrong source. Please use 'json', 'csv', or 'sql'."

        if product_id:
            filtered_products = [p for p in products_data if p['id'] == product_id]
            if not filtered_products:
                error_message = "Product not found."
            products_data = filtered_products

        return render_template('product_display.html', products=products_data, error=error_message)

    if __name__ == '__main__':
        app.run(debug=True, port=5000)
    ```

4.  **Run the Flask application:** Execute `python3 task_04_db.py` and navigate to `http://127.0.0.1:5000/products?source=sql`.
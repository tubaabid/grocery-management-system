from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary data store (in memory)
grocery_items = []

@app.route('/')
def index():
    total = sum(item['price'] * item['quantity'] for item in grocery_items)
    return render_template('index.html', items=grocery_items, total=total)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    grocery_items.append({'name': name, 'price': price, 'quantity': quantity})
    return redirect(url_for('index'))

@app.route('/clear')
def clear_items():
    grocery_items.clear()
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if 0 <= index < len(grocery_items):
        grocery_items.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

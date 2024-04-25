from  flask import Flask, render_template

#flask instance
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/dash')
def dashboard():
    return render_template('dashboard.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

app.run(debug=True)

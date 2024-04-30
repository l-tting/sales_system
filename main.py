from  flask import Flask, render_template,redirect,url_for,request,flash

from database import get_data,insert_products,insert_sales

#flask instance
app = Flask(__name__)
app.secret_key = 'djdjdk68899'
#route is used to link url with function


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    products = get_data('products')
    return render_template('products.html',products = products)

@app.route('/dash')
def dashboard():
    return render_template('dashboard.html')

@app.route('/sales')
def sales():
    sales = get_data('sales')
    products = get_data('products')
    return render_template('sales.html', sales = sales,products=products)

# @app.route("/<name>/")
# def home(name):
#     return render_template('test.html',content=name)

@app.route('/add_products', methods=['GET','POST'])
def add_prods():
    p_name = request.form['prod']
    b_price = request.form['buying']
    s_price = request.form['selling']
    s_quantity = request.form['stock']
    new = (p_name,b_price,s_price,s_quantity)
    insert_products(new)
    flash(f'{s_quantity} {p_name} added successfully')
    return redirect(url_for('products'))


@app.route('/make_sale',methods= ['GET','POST'])
def make_sale():
    #get form data
    pid = request.form['select']
    quantity = request.form['quantity']

    new_sale = (pid,quantity)
    insert_sales(new_sale)
    return redirect(url_for('sales'))







app.run(debug=True)

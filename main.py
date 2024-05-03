from  flask import Flask, render_template,redirect,url_for,request,flash

from database import get_data,insert_products,insert_sales,profit_per_product,profit_per_day,sales_per_day,sales_per_prod

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
    p_prod = profit_per_product()
    p_day = profit_per_day()
    s_day = sales_per_day()
    s_prod = sales_per_prod()
    # print(s_day)
    print(s_prod)
    # print(p_day)
    # print(p_prod)
    p_name = []
    p_profit = []
    day = []
    d_profit = []
    sales_day = []
    sales_prod = []
    x = []
    y = []
    for i in p_prod:
        p_name.append(i[0])
        p_profit.append(i[1])
    
    for i in p_day:
        day.append(str(i[0]))
        d_profit.append(i[1])

    for i in s_day:
        sales_day.append(str(i[0]))
        sales_prod.append(i[1])

    for i in s_prod:
        x.append(i[0])
        y.append(i[1])
    return render_template('dashboard.html',name=p_name,profit=p_profit,day = day,d_profit=d_profit,pro_name=x,pro_sales=y,sales_prod=sales_prod)

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
    flash('Sale made successfully')
    return redirect(url_for('sales'))







app.run(debug=True)

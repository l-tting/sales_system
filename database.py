import psycopg2


#connecting to postgressql database
conn = psycopg2.connect(
    dbname = 'MyDuka',
    user = 'postgres',
    password = '6979',
    host = 'localhost',
    port = 5432
)
# open a cursor to perform database operation

cur = conn.cursor()

def get_data(table):
    select = f"select * from {table}"
    cur.execute(select)
    data = cur.fetchall()
    # for i in data:
    #     print(i)
    return data
data = get_data('products')
# print(data)

   
def insert_products(values):
    insert = f"insert into products(name,buying_price,selling_price,stock_quantity)values{values}"
    cur.execute(insert)
    conn.commit()
product_val = ("milk",20,30,100)
# insert_products(product_val)
get_data("products")
get_data("sales")

def insert_products(values):
    insert = "insert into products(name,buying_price,selling_price,stock_quantity)values(%s,%s,%s,%s)"
    cur.execute(insert,values)
    conn.commit()
product_val = ("meat",20,30,100)
insert_products(product_val)
get_data("products")

get_data("sales")

# create a function to insert sales in 2 ways
    # meth 1
def insert_sales(val):
    insert = f"insert into sales(pid,quantity,created_at)values{val}"
    cur.execute(insert)
    conn.commit()
sale_val = (2,18,"now()")
# insert_sales(sale_val)
get_data("sales")
     
    #meth 2
def insert_sales(val):
    insert = "insert into sales(pid,quantity,created_at)values(%s,%s,now())"
    cur.execute(insert,val)
    conn.commit()
# sal = (1,33,"now()")
# insert_sales(sal)
# get_data("sales")
    
def profit_per_product():
    profit = 'Select name,SUM((selling_price-buying_price) * stock_quantity)as profit  from sales join products on sales.pid=products.id GROUP BY name;'
    cur.execute(profit)
    data = cur.fetchall()
    return data
prof = profit_per_product()
# print(prof)

def profit_per_day():
    per_day = 'select DATE(created_at) as days,sum((selling_price-buying_price)*(quantity)) as profit from products join sales on sales.pid=products.id group by days order by days;'
    cur.execute(per_day)
    data = cur.fetchall()
    return data
per_d = profit_per_day()
# print(per_d)

def sales_per_prod():
    sale = 'select name,sum(selling_price*quantity) as p_sales from sales join products on sales.pid = products.id group by name;'
    cur.execute(sale)
    data = cur.fetchall()
    return data
s_prod = sales_per_prod()
# print(s_prod)

def sales_per_day():
    sale = 'select DATE(created_at) as day,sum(selling_price*quantity) as d_sales from sales join products on sales.pid=products.id group by day;'
    cur.execute(sale)
    data = cur.fetchall()
    return data
s_day = sales_per_day()
# print(s_day)


def insert_user(values):
    query = 'insert into users(full_name,email,password)values(%s,%s,%s)'
    cur.execute(query,values)
    conn.commit()

def check_email(email):
    query = 'select * from users where email = %s'
    cur.execute(query,(email,))
    data = cur.fetchone()
    return data

def get_name(nm):
    name = 'select * from products where name=%s '
    cur.execute(name,(nm,))
    data = cur.fetchall()
    return data
# x = get_name()
# print(x)

def update_prod(name):
    query = f'update products set name=%s, buying_price= %s, selling_price=%s , stock_quantity=%s where name = {name}'
    cur.execute(query)
    conn.commit()

def check_email_exist(email):
    query = 'select * from users where email = %s'
    cur.execute(query,(email,))
    data = cur.fetchall()
    return data

# ch=check_email_exist("ropu")
# print(ch)

def check_email_pass(email,password):
    query = 'select * from users where email=%s and password=%s'
    cur.execute(query,(email,password))
    data = cur.fetchall()
    return data 
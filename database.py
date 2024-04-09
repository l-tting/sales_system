import psycopg2


#connecting to postgressql database
conn = psycopg2.connect(
    dbname = 'my_duka',
    user = 'postgres',
    password = '6979',
    host = 'localhost',
    port = 5432
)
# open a cursor to perform database operation

cur = conn.cursor()

def get_products():
    select = 'select * from products'
    cur.execute(select)
    prods = cur.fetchall()
    for i in prods:  
        print(i)
# get_products()

def get_sales():
    select = 'select * from sales'
    cur.execute(select)
    sales = cur.fetchall()
    for i in sales:
        print(i)
# get_sales()

# insert_sales()
# get_sales()
def get_data(table):
    select = f"select * from {table}"
    cur.execute(select)
    data = cur.fetchall()
    for i in data:
        print(i)

   
# def insert_products(values):
#     insert = f"insert into products(name,buying_price,selling_price,stock_quantity)values{values}"
#     cur.execute(insert)
#     conn.commit()
# product_val = ("milk",20,30,100)
# insert_products(product_val)
# get_data("products")
# get_data("sales")

def insert_products(values):
    insert = "insert into products(name,buying_price,selling_price,stock_quantity)values(%s,%s,%s,%s)"
    cur.execute(insert,values)
    conn.commit()
# product_val = ("meat",20,30,100)
# insert_products(product_val)
# get_data("products")
# get_data("sales")

# create a function to insert sales in 2 ways
    # meth 1
def insert_sales(val):
    insert = f"insert into sales(pid,quantity,created_at)values{val}"
    cur.execute(insert)
    conn.commit()
sale_val = (2,18,"now()")
insert_sales(sale_val)
get_data("sales")
     
    #meth 2
def insert_sales(val):
    insert = "insert into sales(pid,quantity,created_at)values(%s,%s,%s)"
    cur.execute(insert,val)
    conn.commit()
sal = (1,33,"now()")
# insert_sales(sal)
# get_data("sales")
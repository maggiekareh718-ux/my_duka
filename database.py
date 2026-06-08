import psycopg2

#establishing a connection to a postgres
conn=psycopg2.connect(host='localhost',port=5432,user='postgres',password='13918',dbname='myduka')

#cur object
cur=conn.cursor()
def get_products():
    cur.execute("select * from products")
    products_data =cur.fetchall()
    return products_data

cur=conn.cursor()
def get_sales():
    cur.execute("select * from sales")
    sales_data=cur.fetchall()
    return sales_data

#this
#cur.execute("insert into products(name,buying_price,selling_price)values('Cap',300,500)")
#conn.commit()
#print(products_data)

#or this
def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()

product1=('toys',600,800)
product2=('maize',150,300)

insert_products(product1)
insert_products(product2)
print(products_data)

def insert_products2(values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",values)
    conn.commit()

product3=('phone',10000,30000)
insert_products2(product3)

print(products_data)

def insert_sales(values):
    cur.execute(f"insert into sales(pid,quantity)values{values}")
    con.commit()

sales1=(3,20)
sales2=(4,32)

insert_sales(sales1)
insert_sales(sales2)

print(sales_data)

def get_stock():
    cur.execute("select * from stock")
    stock_data=cur.fetchall()
    return stock_data

def insert_stock(values):
    cur.execute(f"insert into stock(pid,stock_quantity)values{values}")
    con,commit()

stock1=(3,46)
stock2=(4,78)

insert_stock(stock1)
insert_stock(stock2)

def sales_per_day():
    cur.execute("""
    SELECT DATE(created_at) AS sale_date, SUM(Quantity) AS sales_per_day 
    FROM sales GROUP BY DATE(created_at) ORDER BY sale_date;
    """)
    daily_sales=cur.fetchall()
    return daily_sales



def profit_per_day():
    cur.execute("""
    SELECT DATE(sales.created_at) AS sale_date, SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit_per_day
    FROM sales JOIN products ON sales.pid = products.id GROUP BY DATE(created_at) ORDER BY sale_date;
    """)
    daily_profit=cur.fetchall()
    return daily_profit


def sales_per_product():
    cur.execute("""
    SELECT name, SUM(sales.quantity) AS sales_per_product
    FROM sales JOIN products ON sales.pid = products.id GROUP BY name;
    """)

    product_sales=cur.fetchall()
    return product_sales


def  profit_per_product():
    cur.execute("""
    SELECT name, SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit_per_product 
    FROM sales JOIN products ON sales.pid = products.id GROUP BY name;
    """)

    product_profit=cur.fetchall()
    return product_profit
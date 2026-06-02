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



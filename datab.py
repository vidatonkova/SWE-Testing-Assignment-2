import sqlite3


def databasing():
    connection = sqlite3.connect('accounting.db')
    cur = connection.cursor()

    cur.execute(""" CREATE TABLE IF NOT EXISTS customer (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            total_goods_bought integer
                                        ); """)

    cur.execute(""" CREATE TABLE IF NOT EXISTS orders (
                                                customer_id integer PRIMARY KEY,
                                                goods_bought integer
                                            ); """)

    connection.commit()
    cur.close()
    connection.close()


def customerss(id, name, total_goods_bought):
    connection = sqlite3.connect('accounting.db')
    cur = connection.cursor()

    customer_insert = """INSERT INTO customer
                              (id, name, total_goods_bought) 
                              VALUES (?, ?, ?);"""
    data_tuple = (id, name, total_goods_bought)
    cur.execute(customer_insert, data_tuple)

    connection.commit()
    cur.close()
    connection.close()


def orderss(customer_id, goods_bought):
    connection = sqlite3.connect('accounting.db')
    cur = connection.cursor()

    orders_insert = """INSERT INTO orders
                                  (customer_id, goods_bought) 
                                  VALUES (?, ?);"""
    data_tuple = (customer_id, goods_bought)
    cur.execute(orders_insert, data_tuple)

    connection.commit()
    cur.close()
    connection.close()


def retrieve():
    connection = sqlite3.connect('accounting.db')
    cur = connection.cursor()

    # do something
    cur.execute(""" CREATE TABLE IF NOT EXISTS orders (
                                                    customer_id integer PRIMARY KEY,
                                                    goods_bought integer
                                                ); """)

    cur.execute("SELECT * FROM customer")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    connection.commit()
    cur.close()
    connection.close()
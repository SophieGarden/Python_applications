import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database_test1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store1 (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database_test1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES('%s', '%s', '%s' )"%(item, quantity, price))
    cur.execute("INSERT INTO store1 VALUES(%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def delete(item):
    conn = psycopg2.connect("dbname='database_test1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE from store1 where item=%s", (item,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = psycopg2.connect("dbname='database_test1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store1 SET quantity=%s, price=%s WHERE item=%s", (item, quantity, price))
    conn.commit()
    conn.close()

create_table()
insert("coffee cup test", 11, 7)
update(11, 6, "coffee cup")
delete("coffee cup test")

def view():
    conn = psycopg2.connect("dbname='database_test1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store1")
    rows = cur.fetchall()
    conn.close()
    return rows

print(view())

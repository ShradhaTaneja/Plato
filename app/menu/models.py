from app.db import get_mysql_conn

def fetch_categories():
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'SELECT category FROM menu_category'
    cursor.execute(query)

    all_data = []

    for row in cursor.fetchall():
        all_data.append(row[0])

    conn.close()
    return all_data

def category_exists(category):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'SELECT * FROM menu_category where category = \'%s\'' % category
    cursor.execute(query)

    if cursor.fetchone() is None:
        return False
    return True


def insert_category(category):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'INSERT INTO menu_category VALUES (\'%s\')' % category
    cursor.execute(query)
    conn.commit()
    conn.close()


def fetch_menu(rid):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'SELECT category FROM restaurant_menu WHERE rid = %d ' % rid
    cursor.execute(query)

    all_data = []

    for row in cursor.fetchall():
        all_data.append(row[0])

    conn.close()
    return all_data

def insert_menu(rid, category):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'INSERT INTO restaurant_menu (rid, category) VALUES (%d, \'%s\')' % (rid, category)
    cursor.execute(query)
    conn.commit()
    conn.close()


def delete_menu(rid, mcategory):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'DELETE FROM restaurant_menu WHERE rid = %d AND category = \'%s\';' % (rid, mcategory)
    cursor.execute(query)
    conn.commit()
    conn.close()


def rest_category_exists(rid, category):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'SELECT * FROM restaurant_menu WHERE rid = %d AND category = \'%s\'' % (rid, category)
    cursor.execute(query)
    if cursor.fetchone() is None:
        return False
    return True


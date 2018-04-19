from app.db import get_mysql_conn

def fetch_all_menu_items(rid):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'SELECT item_id, category, name, price from menu_items where rid = %d ' % rid
    cursor.execute(query)

    all_data = {}

    for row in cursor.fetchall():
        item_details = {}
        item_details['id'] = row[0]
        item_details['name'] = row[2]
        item_details['price'] = row[3]

        if row[1] not in all_data:
            all_data[row[1]] = []
        all_data[row[1]].append(item_details)

    conn.close()
    return all_data


def insert_menu_item(data):
    conn = get_mysql_conn()
    cursor = conn.cursor()

    input_columns = data.keys()

    input_column_data = []

    for col in input_columns:
        input_column_data.append(col)

    input_column_data = 'item_id, rid, category, name, price'
    input_value_data = '\'%s\', %d, \'%s\',\'%s\',\'%s\'' % (data['item_id'], int(data['rid']), str(data['category']), str(data['name']), str(data['price']))

    insert_query = 'INSERT INTO `menu_items` (%s) values (%s);' % (input_column_data, input_value_data)

    cursor.execute(insert_query)
    conn.commit()
    conn.close()
    return True

def fetch_category_menu_items(rid, mcategory):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'SELECT item_id, name, price FROM menu_items WHERE rid = %d AND category = \'%s\' ' % (rid, mcategory)
    cursor.execute(query)
    all_data = []

    for row in cursor.fetchall():
        item_details = {}
        item_details['id'] = row[0]
        item_details['name'] = row[1]
        item_details['price'] = row[2]

        all_data.append(item_details)

    conn.close()
    return all_data

def fetch_item(rid, item_id):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'SELECT item_id, category, name, price from menu_items where rid = %d AND item_id = \'%s\'' % (rid, item_id)
    cursor.execute(query)

    all_data = []

    for row in cursor.fetchall():
        item_details = {}
        item_details['id'] = row[0]
        item_details['category'] = row[1]
        item_details['name'] = row[2]
        item_details['price'] = row[3]
        all_data.append(item_details)

    conn.close()
    return all_data

def delete_menu_item(rid, mcategory, item_id):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'DELETE FROM menu_items WHERE rid = %d AND category = \'%s\' AND item_id = \'%s\';' % (rid, mcategory, item_id)
    cursor.execute(query)
    conn.commit()
    conn.close()

from app.db import get_mysql_conn

def fetch_all_menu_items(rid):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'SELECT id, menu_category, name, price from menu_items where rid = %d ' % rid
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

def fetch_specific_menu_items(rid, mcategory):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'SELECT id, name, price from menu_items where rid = %d and menu_category = %s ' % (rid, mcategory)
    all_data = []

    for row in cursor.fetchall():
        item_details = {}
        item_details['id'] = row[0]
        item_details['name'] = row[1]
        item_details['price'] = row[2]

        all_data.append(item_details)

    conn.close()
    return all_data

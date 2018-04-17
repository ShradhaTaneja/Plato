from app.db import get_mysql_conn

def fetch_all_menu(rid):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'SELECT DISTINCT(menu_category) FROM menu_items WHERE rid = %d ' % rid
    cursor.execute(query)

    all_data = []

    for row in cursor.fetchall():
        all_data.append(row[0])

    conn.close()
    return all_data


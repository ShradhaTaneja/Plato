from app.db import get_mysql_conn

def exists(rid):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'select rid, rname, raddress, rcity, rstate, rating, rcontact, rwebsite, remail from restaurant where rid = %d ;' % int(rid)
    cursor.execute(query)

    if cursor.fetchone() is None:
        return False
    return True


def fetch_all_restaurants():
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'select rid, rname, raddress, rcity, rstate, rating, rcontact, rwebsite, remail from restaurant;'
    cursor.execute(query)

    all_data = []

    for row in cursor.fetchall():
        row_data = {}
        row_data['rid'] = row[0]
        row_data['name'] = row[1]
        row_data['address'] = row[2]
        row_data['city'] = row[3]
        row_data['state'] = row[4]
        row_data['rating'] = row[5]
        row_data['contact'] = row[6]
        row_data['website'] = row[7]
        row_data['email'] = row[8]
        all_data.append(row_data)

    conn.close()
    return all_data


def fetch_restaurant(rid):
    conn = get_mysql_conn()
    cursor = conn.cursor()
    query = 'select rid, rname, raddress, rcity, rstate, rating, rcontact, rwebsite, remail from restaurant where rid =  %s;' % (rid)
    cursor.execute(query)
    data =  cursor.fetchone()
    if data is None:
        return {}
    details = {}
    details['rid'] = data[0]
    details['name'] = data[1]
    details['address'] = data[2]
    details['city'] = data[3]
    details['state'] = data[4]
    details['rating'] = data[5]
    details['contact'] = data[6]
    details['website'] = data[7]
    details['email'] = data[8]

    conn.close()
    return details


def insert_restaurant(data):
    conn = get_mysql_conn()
    cursor = conn.cursor()

    input_columns = data.keys()

    input_column_data = []
    input_value_data = []

    for col in input_columns:
        input_column_data.append(col)
        input_value_data.append(data[col])

    # this is a temp thing, the column name mapping needs to be improved
    insert_query = 'INSERT INTO `restaurant` (%s) values (%s);' % ( "`r" + "`, `r".join(input_column_data) + "`", "'" + "', '".join(input_value_data) + '\'')

    cursor.execute(insert_query)
    conn.commit()

    rid = cursor.lastrowid
    conn.close()
    return rid


def delete_restaurant(rid):
    conn = get_mysql_conn()
    cursor = conn.cursor()

    delete_query = 'DELETE FROM restaurant where rid = %d ' % int(rid)

    cursor.execute(delete_query)
    conn.commit()
    conn.close()

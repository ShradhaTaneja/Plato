from app.db import MySql

def fetch_all_restaurants():
    db = MySql()
    conn = db.get_conn()
    cursor = conn.cursor()
    query = 'select rid, rname, raddress, rcity, rstate, rating, rcontact, rwebsite, remail from restaurant;'
    cursor.execute(query)

    all_data = []

    for row in cursor.fetchall():
        row_data = {}
        row_data['rid'] = row[0]
        row_data['rname'] = row[1]
        row_data['raddress'] = row[2]
        row_data['rcity'] = row[3]
        row_data['rstate'] = row[4]
        row_data['rating'] = row[5]
        row_data['rcontact'] = row[6]
        row_data['rwebsite'] = row[7]
        row_data['remail'] = row[8]
        all_data.append(row_data)

    db.close()
    return all_data


def fetch_restaurant(rid):
    db = MySql()
    conn = db.get_conn()
    cursor = conn.cursor()
    query = 'select rid, rname, raddress, rcity, rstate, rating, rcontact, rwebsite, remail from restaurant where rid =  %s;' % (rid)
    cursor.execute(query)
    data =  cursor.fetchone()

    details = {}
    details['rid'] = data[0]
    details['rname'] = data[1]
    details['raddress'] = data[2]
    details['rcity'] = data[3]
    details['rstate'] = data[4]
    details['rating'] = data[5]
    details['rcontact'] = data[6]
    details['rwebsite'] = data[7]
    details['remail'] = data[8]

    db.close()
    return details


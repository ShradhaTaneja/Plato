from app.db import MySql

def get_all_restaurants():
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

    return all_data



import app.config as config
import MySQLdb

def get_mysql_conn():
    conn = MySQLdb.connect(host = config.MYSQL_CREDS['HOST'], user = config.MYSQL_CREDS['USER'], db = config.MYSQL_CREDS['DATABASE'], passwd = config.MYSQL_CREDS['PASSWORD'])
    return conn


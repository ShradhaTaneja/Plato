import MySQLdb
import config

class MySql:
    def __init__(self):
        pass
    def get_conn(self):
        conn = MySQLdb.connect(host = config.MYSQL_CREDS['HOST'], user = config.MYSQL_CREDS['USER'], db = config.MYSQL_CREDS['DATABASE'], passwd = config.MYSQL_CREDS['PASSWORD'])
        return conn

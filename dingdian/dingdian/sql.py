import MySQLdb
import time
from dingdian import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB
cnx = ''
cur = ''
try:
    cnx = MySQLdb.Connect(MYSQL_HOSTS, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)
    cur = cnx.cursor()
    print('################connect mysql########################################')
    time.sleep(3)
except ConnectionError as e:
    print(str(e))


class Sql:
    @classmethod
    def insert_dd_name(cls, xs_name, xs_author, category, name_id):
        sql = 'INSERT INTO dd_name (`xs_name`, `xs_author`, `category`, `name_id`) ' \
              'VALUES (%(xs_name)s, %(xs_author)s, %(category)s, %(name_id)s)'
        value = {
            'xs_name': xs_name,
            'xs_author': xs_author,
            'category': category,
            'name_id': name_id
        }
        cur.execute(sql, value)
        print('insert data')
        cnx.commit()

    @classmethod
    def select_name(cls, name_id):
        sql = "SELECT EXISTS(SELECT 1 FROM dd_name WHERE name_id=%(name_id)s)"
        value = {'name_id': name_id}
        cur.execute(sql, value)
        for name_id in cur:
            return name_id[0]

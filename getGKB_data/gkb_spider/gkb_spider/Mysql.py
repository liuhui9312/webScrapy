import MySQLdb
from gkb_spider import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = MySQLdb.connect(host=MYSQL_HOSTS, user=MYSQL_USER,
                      passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset='utf8')
cur = cnx.cursor()
print('login mysql!#############################3')

class Sql:

    @classmethod
    def insert_pharmgkb(cls, items, num):
        sql = "INSERT INTO pharmgkb (`pa_id`, `num`, `genes`, `chemicals`, `pvalue`, `literature`, `significance`," \
              "`phenotypeCategories`, `variants`, `cases`, `race`, `characteristics`, `sentence`," \
              " `literatureUrl`, `id`)" \
              " VALUES (%(pa_id)s, %(num)s, %(genes)s, %(chemicals)s, %(pvalue)s, %(literature)s, %(significance)s, " \
              "%(phenotypeCategories)s, %(variants)s, %(cases)s, %(race)s, %(characteristics)s, %(sentence)s, " \
              "%(literatureUrl)s, %(id)s)"
        value = {
            'pa_id': items['pa_id'],
            'num': num,
            'genes': items['genes'][num],
            'chemicals': items['chemicals'][num],
            'pvalue': items['pvalue'][num],
            'literature': items['literature'][num],
            'significance': items['significance'][num],
            'phenotypeCategories': items['phenotypeCategories'][num],
            'variants': items['variants'][num],
            'cases': items['cases'][num],
            'race': items['race'][num],
            'characteristics': items['characteristics'][num],
            'sentence': items['sentence'][num],
            'literatureUrl': items['literatureUrl'][num],
            'id': items['id'][num]
        }
        # print(sql%value)
        try:
            cur.execute(sql, value)
            cnx.commit()
        except Exception as e:
            print(str(e))


    @classmethod
    def select_name(cls, items, num):
        try:
            sql = "SELECT EXISTS(SELECT 1 FROM pharmgkb " \
                  "WHERE pa_id=%(pa_id)s AND num=%(num)s)"
            value = {
                'pa_id': items['pa_id'],
                'num': num
            }
            cur.execute(sql, value)
            for name_id in cur:
                return name_id[0]
        except Exception as e:
            print(str(e))
'''
    @classmethod
    def select_paId(cls, items, paid):
        try:
            sql = "SELECT EXISTS(SELECT 1 FROM pharmgkb WHERE pa_id=%(pa_id)s)"
            value = {
                'pa_id': paid
            }
            cur.execute(sql, value)
            for name_id in cur:
                return name_id[0]
        except Exception as e:
            print(str(e))
'''

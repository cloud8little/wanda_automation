import pymysql.cursors
import sys
from configuration.globalUtil import GlobalSetting

default_config = GlobalSetting.get_value('')
env = 'SIT'
env_config = default_config[env]

class MysqlLib:
    def __init__(self,host,user,password):
        try:
            self.connection = pymysql.connect(host=host,
                                         user=user,
                             password=password,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        except pymysql.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)

    def execute_sql(self,sql_sentence,database="loanpublic",parameters=None):
        cursor = self.connection.cursor()
        self.connection.select_db(database)
        try:
            with cursor as cursor:
                if parameters:
                    cursor.execute(sql_sentence,parameters)
                else:
                    cursor.execute(sql_sentence)
                self.connection.commit()
        finally:
            cursor.close()
            return cursor

    def close_conn(self):
        self.connection.close()

if __name__ == '__main__':
    mysql_config = env_config['MYSQL']
    mysql_conn = MysqlLib(mysql_config['host'],mysql_config['username'],mysql_config['password'])
    sql_sample_1 = "select count(*) from loancore.user_auth_id_symbol a where  a.IDENTIFIERS>='13320045098' and a.IDENTIFIERS<='13320086261';"
    mysql_conn.execute_sql(sql_sample_1,'loancore')
    sql_sample_2 = "select a.relation_mobile,a.resource_id from loancore.user_financial_instruments_info a where CREATE_TIME >= '2017-11-02 19:50' order by RELATION_MOBILE limit 10;"
    cursor_2 = mysql_conn.execute_sql(sql_sample_2,'loanpublic')

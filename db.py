from http import server
import pymssql


class db:
    server = 'TAWSQLDBA01\TAMSSDBA01'
    database = 'MTB_TEST_EE'
    username = 'Mtbtestee'
    password = 'Aa12366@'

    def __init__(self):
        self.conn = pymssql.connect(
            self.server, server.user, server.password, server.database)
        self.cur = self.conn.cursor()

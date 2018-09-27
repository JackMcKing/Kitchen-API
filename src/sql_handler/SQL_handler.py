import sqlite3

class SQL_handler:

    def __init__(self, path, **kw):
        self.path = path
        for k,w in kw.items():
            setattr(self,k,w)

        self.conn = sqlite3.connect(path)
        self.c = self.conn.cursor()

    
    def create_table(self, table_name, **column):
        conn = self.conn
        c = self.c

        c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)'''.format())


    def readdata(self):
        conn = self.conn
        c = self.c

        c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
        c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        conn.commit()
        conn.close()

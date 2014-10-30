#MySqlMethods
#A module for the Python Fitness Planner application
#Todd Pettit 10/25/2014
#----------------------------------------------------------------------------------------------------------------------#

import MySQLdb


class DbConn(object):
    conn = None
    cursor = None

    def logon(self, host, username, password, db):
        DbConn.conn = MySQLdb.connect(host, username, password, db)
        DbConn.cursor = DbConn.conn.cursor()

    def logoff(self):
        if DbConn.conn is not None:
            DbConn.conn.close()

    def store_user(self, first_name, last_name, gender, height, weight, age):
        sqlstatement = """INSERT INTO USERS (firstName, lastName, gender, height, weight, age)
                            VALUES ('%s', '%s', '%s', %d, %d, %d);""" % (first_name, last_name, gender, height, weight, age)
        try:
            DbConn.cursor.execute(sqlstatement)
            DbConn.conn.commit()
        except Exception as e:
            print e
            DbConn.conn.rolback()

    def get_metric(self, email, metric):
        sqlstatement = """SELECT %s FROM USERS
                          WHERE email ='%s';""" % (metric, email)
        DbConn.cursor.execute(sqlstatement)
        data = DbConn.cursor.fetchone()
        return data[0]

    def update_metric(self, email, metric, value):
        sqlstatement = """UPDATE USERS
                            SET %s='%s'
                            WHERE email='%s'""" % (metric, value, email)
        try:
            DbConn.cursor.execute(sqlstatement)
            return True
        except:
            DbConn.conn.rollback()
            return False

def main():
    conn = DbConn()
    conn.logon("127.0.0.1", "adminPAlFsvm", "fAxAYtF8zmSX", "python")
    #print conn.check_name("Todd")
    #conn.store_user("Todd", "Pettit", "m", 172, 190, 23)
    print conn.get_metric("todd.pettit@hotmail.com", "weight")
    conn.update_metric("todd.pettit@hotmail.com", "weight", 195)
    print conn.get_metric("todd.pettit@hotmail.com", "weight")
    conn.logoff()

if __name__ == "__main__":
    main()
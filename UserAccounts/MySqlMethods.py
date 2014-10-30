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

    def check_name(self, first_name):
        sqlstmnt = """SELECT firstName FROM USERS
                      WHERE firstName='%s'""" % first_name
        DbConn.cursor.execute(sqlstmnt)
        data = DbConn.cursor.fetchone()
        return data

    def store_user(self, first_name, last_name, gender, height, weight, age):
        sqlstatement = """INSERT INTO USERS (firstName, lastName, gender, height, weight, age)
                            VALUES ('%s', '%s', '%s', %d, %d, %d);""" % (first_name, last_name, gender, height, weight, age)
        try:
            DbConn.cursor.execute(sqlstatement)
            DbConn.conn.commit()
        except Exception as e:
            print e
            DbConn.conn.rolback()

    def select_user(self, first_name):
        sqlstatement = """SELECT firstName FROM USERS
                          WHERE firstName='%s'
        """ % first_name
        DbConn.cursor.execute(sqlstatement)
        data = DbConn.cursor.fetchone()
        if data is not None:
            return first_name
        else:
            print "This user does not exist in our database. Please create a user and try again."
            return data

    def user_gender(self, first_name):
        sqlstatement = """SELECT gender FROM USERS
                          WHERE firstName='%s'
        """ % first_name
        DbConn.cursor.execute(sqlstatement)
        data = DbConn.cursor.fetchone()
        return data[0]

    def user_weight(self, first_name):
        sqlstatement = """SELECT weight FROM USERS
                          WHERE firstName='%s'
        """ % first_name
        DbConn.cursor.execute(sqlstatement)
        data = DbConn.cursor.fetchone()
        return data[0]

    def user_height(self, first_name):
        sqlstatement = """SELECT height FROM USERS
                          WHERE firstName='%s'
        """ % first_name
        DbConn.cursor.execute(sqlstatement)
        data = DbConn.cursor.fetchone()
        return data[0]

    def user_age(self, first_name):
        sqlstatement = """SELECT age FROM USERS
                          WHERE firstName='%s'
        """ % first_name
        DbConn.cursor.execute(sqlstatement)
        data = DbConn.cursor.fetchone()
        return data[0]


def main():
    conn = DbConn()
    conn.logon("127.0.0.1", "adminPAlFsvm", "fAxAYtF8zmSX", "python")
    print conn.check_name("Todd")
    #conn.store_user("Todd", "Pettit", "m", 172, 190, 23)
    print conn.user_age("Todd")
    print conn.user_height("Todd")
    print conn.user_weight("Todd")
    print conn.user_gender("Todd")
    conn.logoff()

if __name__ == "__main__":
    main()
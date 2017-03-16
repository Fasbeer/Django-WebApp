import MySQLdb

class DBConnection:

    def __init__(self):

        self.db = MySQLdb.connect("nathanwc1h0aq.cimqbjokw91n.us-west-2.rds.amazonaws.com",
                             "nathan",
                             "Ox38beOx3",
                             "nathansDB")

        self.cursor = self.db.cursor()

    def select(self):
        sql = "SELECT * FROM nathansDB.main;"
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = self.cursor.fetchall()
            out = []
            for row in results:
                out.append(row[0] + ", " + row[2] + ", " + row[3])
            return out

        except:
            print "Error: unable to fecth data"

			
    def insert(self, author, publishDate, title, publisher, page):

        sql = "INSERT INTO nathansDB.main VALUES ('" \
              + author + "', '" \
              + publishDate + "', '" \
              + title + "', '" \
              + publisher + "', " \
              + page + \
              ");"
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Commit your changes in the database
            self.db.commit()
        except:
            # Rollback in case there is any error
            self.db.rollback()

    def close(self):
        # disconnect from server
        self.db.close()

    #delete title from database
    def delete(self, title):

        sql = "DELETE FROM `nathansDB`.`main` " \
              "WHERE `TITLE` = '" + title + "'" \

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()


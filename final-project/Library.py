import mysql.connector
class Library:
    def __init__(self, HOST, USERNAME, PASSWORD, DATABASE):
        self.HOST = HOST
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.DATABASE = DATABASE

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.HOST,
                user=self.USERNAME,
                password=self.PASSWORD,
                database=self.DATABASE
            )
            if connection.is_connected():
                print("Connected to the MySQL database!")
                return connection

        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")

        # finally:
        #     if 'connection' in locals() and connection.is_connected():
        #         connection.close()
        #         print("MySQL connection is closed")
        #         return None

    def select(self,connection):
        try:
            cursor = connection.cursor()
            cursor.execute("""SELECT b.book_name AS 'Book', CONCAT(a.author_fname,' ',a.author_lname) AS 'Author Name'
                     FROM book b
                    INNER JOIN author a
                    ON b.author_id = a.author_id;
                    """)
            book_author = cursor.fetchall()
            for data in book_author:
                print(f"Book Name: {data[0]}, Author Name: {data[1]}")
        except mysql.connector.Error as e:
            print(f"Error showing Books and Author names. Error: {e}")
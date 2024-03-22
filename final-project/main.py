from Library import *
import Library as lib

USERNAME = "root"
PASSWORD = "1234"
HOSTNAME = "localhost"
DATABASE_NAME = "books"

data = lib.Library(HOSTNAME, USERNAME, PASSWORD, DATABASE_NAME)
connection = data.connect()
data.select(connection)

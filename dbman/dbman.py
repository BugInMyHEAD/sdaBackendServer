import pymysql

class recipe_db_connection:
    
    def __init__(self, *args, **kwargs):
        self.db_obj = None
        #return super().__init__(*args, **kwargs)

    def insert_recipe(self, likes:list, dislikes:list, addible:bool):
        """likes and dislikes are ingredients_id list"""

# Open database connection
db = pymysql.connect(
    host='localhost', port=3306, user='root', passwd='1111', db='sdadb',
    charset='utf8', autocommit=True)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()

import pip 
   
class Retrieve(object):
    def __init__(self, database, list_objects, periods = None):
        self.database = database
        self.list_objects = "SELECT * from" + " " + str(list_objects)
        self.periods = periods
    
    def connection(self):
        if type(self.database) != str:
            database = str(self.database)
        try:
            con = psycopg2.connect(database= self.database,
                                   user="postgres",
                                   password="postgres1!",
                                   host="211.48.245.7",
                                   port="5435")
            cur = con.cursor()
            return cur
        except:
            raise ConnectionError

    def query(self):
        cur = self.connection()
        cur.execute(self.list_objects)
        rows = cur.fetchall()
        records = len(rows)

        columns = [desc[0] for desc in cur.description]
        df = pd.DataFrame(rows, columns = columns)
        return df

def require(packages):
    try:
        __import__(packages)
    execept ImportError:
        pip.main(["install", packages])

class preprocessing(object):
    def __init__(self, data):
        self.data = data

    if self.data



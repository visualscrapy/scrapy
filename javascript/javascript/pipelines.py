# ====================postgresql storage Start ======================
import psycopg2
class JavascriptPipeline:
    def process_item(self, item, spider):
        return item
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        # self.conn = psycopg2.connect(user = "postgres",password = "7728264",host = "127.0.0.1",port = "5432",database = "myquotes")
        self.conn = psycopg2.connect(user = "ytwahnkwrdcpsi",
                                     password = "a53a5ee07c84a293242c3ef65040c3a7a2a4087d38be11c0b9ff7187d61b2f8d",
                                     host = "ec2-52-71-55-81.compute-1.amazonaws.com",
                                     port = "5432",
                                     database = "d5tf3l9r19qqpt")

        self.curr = self.conn.cursor()
    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(title text,author text,tag text,url text)""")
    def process_item(self, item, spider):
        self.store_db(item)  # used to store the data using this method
        return item
    def store_db(self, item):
        self.curr.execute(""" insert into quotes_tb values(%s, %s,%s)""",(
            item['title'],
            item['author'],
            item['tags'][0] if item['tags'] else '',

        ))
        self.conn.commit()
# ====================postgresql storage End ======================

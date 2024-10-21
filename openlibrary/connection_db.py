import psycopg


class AppContext:
    
    def __init__(self):
        self.conn = psycopg.connect("postgresql://soumaya:root@localhost:5432/BooksDb", autocommit=True)
    def __enter__(self):
        return self.conn
    def __exit__(self, type, value, traceback):
        self.conn.close()
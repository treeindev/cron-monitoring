import psycopg2

class Database:
    def __init__(self):
        # TODO: Externalise database credentials outside from logic
        self.host="localhost"
        self.name="cron_monitoring"
        self.user=""
        self.password=""
        self.connection=None
        self.cursor=None
    
    def connect(self):
        self.connection = psycopg2.connect(
            f"dbname={self.name} user={self.user} host={self.host} password={self.password}"
        )
        self.cursor=self.connection.cursor()
    
    def query(self, query, params=()):
        if not self.cursor:
            raise RuntimeError("Database has not been connected.")

        self.cursor.execute(query, params)
        return self.cursor

    def close(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
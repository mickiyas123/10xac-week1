import psycopg2
from sqlalchemy import create_engine, text


class ConnectToDatabase:
    def __init__(self, db_params):
        try:
            self.engine = create_engine(
                f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"
            )
        except Exception as error:
            raise Exception("Cannot connect to the database. Please try again.")
    def get_engine(self):
        return self.engine

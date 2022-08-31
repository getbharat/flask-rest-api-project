from src.config import config
import cx_Oracle


class ConnectionFactory:

    def __init__(self):
        pass

    # Create session pool
    pool = cx_Oracle.SessionPool(config.username, config.password, config.dsn, min=100, max=100, increment=0,
                                 encoding=config.encoding)

    def get_connection(self):
        return self.pool.acquire()


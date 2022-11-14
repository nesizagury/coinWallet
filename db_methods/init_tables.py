import psycopg2

from db_methods import CONNECTION
from db_methods.init_queries import WALLET_TABLE


def init_method():
    conn = None
    try:
        conn = psycopg2.connect(CONNECTION)
        cursor = conn.cursor()

        cursor.execute(WALLET_TABLE)
        conn.commit()
    finally:
        if conn is not None:
            conn.close()

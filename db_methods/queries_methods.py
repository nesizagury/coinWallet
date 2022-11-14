import random
import time

import psycopg2
from db_methods import CONNECTION
import pandas
from urllib.request import Request, urlopen

from db_methods.df_sql import update_table


def add_address_to_db(address):
    conn = None
    try:
        print(f'adding address={address}')
        conn = psycopg2.connect(CONNECTION)
        cursor = conn.cursor()

        cursor.execute(f"""
            INSERT INTO WALLET(ADDRESS, LAST_TRANSACTION, BALANCE)
            VALUES ('{address}', NULL, NULL) on conflict do nothing;
        """)

        conn.commit()
        print(f'finished adding address={address}')
        cursor.close()
    finally:
        if conn is not None:
            conn.close()


def remove_address_from_db(address):
    conn = None
    try:
        print(f'removing address={address}')
        conn = psycopg2.connect(CONNECTION)
        cursor = conn.cursor()

        cursor.execute(f"""
            DELETE FROM WALLET WHERE ADDRESS='{address}';
        """)

        conn.commit()
        print(f'finished removing address={address}')
        cursor.close()
    finally:
        if conn is not None:
            conn.close()


def sync_addresses_in_db():
    conn = None
    try:
        conn = psycopg2.connect(CONNECTION)
        cursor = conn.cursor()

        cursor.execute(f"""
        SELECT ADDRESS
            FROM WALLET;
        """)
        records = cursor.fetchall()
        conn.commit()

        list_of_dicts = []
        for row in records:
            address = row[0]
            transactions_url = 'https://blockchain.info/rawaddr/' + address
            df = pandas.read_json(transactions_url)
            transactions = df['txs']
            request = Request(f'https://blockchain.info/q/addressbalance/{address}')
            response_body = urlopen(request).read()
            list_of_dicts.append({"ADDRESS": address, "LAST_TRANSACTION": transactions[0]['hash'],
                                  "BALANCE": int(response_body.decode("utf-8"))})
            time.sleep(random.uniform(1, 3))
        df = pandas.DataFrame(list_of_dicts)
        update_table(df, "WALLET", cursor, conn)
        cursor.close()
    finally:
        if conn is not None:
            conn.close()

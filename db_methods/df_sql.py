import psycopg2


def update_table(df, table, cur, conn):
    """
    Using cursor.executemany() to insert the dataframe
    """
    # Create a list of tupples from the dataframe values
    tuples = list(set([tuple(x) for x in df.to_numpy()]))

    # Comma-separated dataframe columns
    cols = ','.join(list(df.columns))
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s)" % (
        f'{table}_TEMP', cols)

    try:
        cur.execute(f"""CREATE TEMP TABLE {table}_TEMP(ADDRESS TEXT PRIMARY KEY     NOT NULL,
            LAST_TRANSACTION            TEXT,
            BALANCE        BIGINT) ON COMMIT DROP""")
        cur.executemany(query, tuples)
        cur.execute(f"""
            UPDATE {table}
            SET last_transaction={table}_TEMP.last_transaction, balance={table}_TEMP.balance
            FROM {table}_TEMP
            WHERE {table}_TEMP.ADDRESS = {table}.ADDRESS;
            """)
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        raise error

from dotenv import load_dotenv

load_dotenv()

WALLET_TABLE = f"""
            CREATE TABLE IF NOT EXISTS WALLET
            (ADDRESS TEXT PRIMARY KEY     NOT NULL,
            LAST_TRANSACTION            TEXT,
            BALANCE        BIGINT);
        """
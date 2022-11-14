"""
flask app handle bitcoin wallet
can add remove addresses, and sync data for them(transactions, balance)
"""

import os

from dotenv import load_dotenv
from flask import Flask, request

from db_methods.init_tables import init_method
from db_methods.queries_methods import add_address_to_db, remove_address_from_db, sync_addresses_in_db

load_dotenv()
app = Flask(__name__)


@app.route('/api/v1/<address>', methods=["POST"])
def add_address(address):
    """
    add bitcoin address to wallet
    @param address: bitcoin address
    @type address: str
    @rtype: str
    """
    if request.method == 'POST':
        add_address_to_db(address)
        return "success"

    return "nothing saved to db"


@app.route('/api/v1/<address>/remove', methods=["POST"])
def remove_address(address):
    """
    remove bitcoin address from wallet
    @param address: bitcoin address
    @type address: str
    @rtype: str
    """
    if request.method == 'POST':
        remove_address_from_db(address)
        return "success"

    return "nothing saved to db"


@app.route('/api/v1/sync', methods=["POST"])
def sync_addresses():
    """
    sync addresses last transaction and balance
    @rtype: str
    """
    if request.method == 'POST':
        sync_addresses_in_db()

    return "success"


if __name__ == "__main__":
    port = int(os.getenv('FLASK_PORT', 5000))
    init_method()
    app.run(debug=True, host="0.0.0.0", port=port)

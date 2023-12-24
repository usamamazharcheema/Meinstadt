import logging

import sql_queries
from utils import db

db = db.db_factory()


def setup_db_schema():
    """Function to setup the database schema."""
    with db.managed_cursor() as cur:
        logging.info("Creating tables")
        for query in sql_queries.create_table_queries:
            cur.execute(query)


def teardown_db_schema():
    """Function to teardown the database schema."""
    logging.info("Dropping tables")
    with db.managed_cursor() as cur:
        for query in sql_queries.drop_table_queries:
            cur.execute(query)

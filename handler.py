import logging
import os

import etl
import run_queries
import schema_manager
from utils import db

db = db.db_factory()


def etl_process(url: str, delay=5):
    """
    Inovke extraction and insertion function

    :param url: URL to fetch data from
    :param delay: Time delay (in seconds) between retries
    :return: None
    """
    alphabet = list(map(chr, range(97, 123)))
    with db.managed_cursor() as cursor:
        for idx, letter in enumerate(alphabet):
            params = {"f": letter}
            data = etl.extraction.fetch_data(url, params, delay)  # Invoking fetch_data
            if data["drinks"] is None:
                continue

            etl.load_db.insertion(cursor, data["drinks"])  # Invoking Inserion method


def main(reset_db, url):
    logging.basicConfig(level="INFO")
    if reset_db == "True":
        schema_manager.teardown_db_schema()
        schema_manager.setup_db_schema()  # setting up database schema

    etl_process(url)  # Performing extraction, measure conversion and data loading

    with db.managed_cursor() as cursor:
        queries_result = run_queries.run_queries(cursor)  # Analytical queries
        return queries_result


def handler(event, context):
    reset_db = os.environ.get("RESET_DB")
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?f="
    queries_result = main(reset_db, url)
    response = {"statusCode": 200, "body": queries_result}

    return response

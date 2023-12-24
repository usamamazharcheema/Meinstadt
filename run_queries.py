from typing import List, Tuple

import pysqlite3 as sqlite3

import sql_queries


def run_queries(cursor: sqlite3.Cursor) -> List[List[Tuple]]:
    """
    Execute a list of SQL Analytical queries and return the results.

    :param cursor: Database cursor
    :return: List of query results
    """

    queries_result = []

    for query in sql_queries.run_queries_list:
        cursor.execute(query)
        result = cursor.fetchall()
        queries_result.append(result)

    return queries_result

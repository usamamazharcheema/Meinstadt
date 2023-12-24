import logging
import time
from typing import Any, Dict, Union

import requests
from requests.exceptions import ConnectionError, HTTPError, RequestException


def fetch_data(
    url: str, params: Dict[str, Any], delay: int, max_retries: int = 3
) -> Union[Dict[str, Any], None]:
    """
    Fetches drinks from Cocktail API endpoint

    :param url: URL to fetch data from
    :param params: alphabetic letter
    :param delay: Time delay (in seconds) between retries
    :param max_retries: Maximum number of retries in case of connection issues
    :returns: Json or None if unsuccessful after max_retries
    """
    response = None
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            logging.error(f"HTTPError: {e}")
            if response and response.status_code == 503:
                logging.info("API is temporarily unavailable. Retrying...")
                time.sleep(delay)
        except ConnectionError as e:
            logging.error(f"ConnectionError: {e}")
            logging.info("Retrying...")
            time.sleep(delay)
        except RequestException as e:
            logging.error(f"RequestException: {e}")
        except Exception as e:
            logging.error(f"Unexpected Error: {e}")
            break

    return None

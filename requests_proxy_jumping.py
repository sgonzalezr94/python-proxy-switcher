from proxy_switcher import ProxySwitcher
from json.decoder import JSONDecodeError
import requests
import time
import logging
import os
from dotenv import load_dotenv


def check_ip():
    try:
        start_time = time.time()
        json_response = requests.get(os.getenv("IP_CHECKER_URL")).json()
        ip = json_response["query"]
        logging.info(
            "Requested completed under IP: %s in %.3f seconds!\n"
            % (ip, (time.time() - start_time))
        )
    except JSONDecodeError:
        logging.error("Request not completed. Failed JSON decoding.\n")


def proxy_job_execution(requests_number: int = 10):
    proxy_switcher = ProxySwitcher(
        os.getenv("PROXY_LIST").strip("][").replace('"', "").split(", "),
        os.getenv("PORT_LIST").strip("][").replace('"', "").split(", "),
    )
    for _ in range(requests_number):
        proxy_switcher.set_proxy()
        check_ip()  # This is meant to be changed to your scrapping job or task that requires proxy-switching


if __name__ == "__main__":
    load_dotenv()
    proxy_job_execution(int(os.environ.get("TOTAL_REQUESTS")))

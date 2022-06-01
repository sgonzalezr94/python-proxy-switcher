from proxy_switcher import ProxySwitcher
from settings import IP_CHECKER_URL, PROXY_LIST, PORT_LIST, NUM_TOTAL_REQUESTS
import json
from json.decoder import JSONDecodeError
import requests
import time


def check_ip():
    try:
        start_time = time.time()
        json_response = requests.get(IP_CHECKER_URL).json()
        ip = json_response["query"]
        print(
            "Requested completed under IP: %s in %.3f seconds!\n"
            % (ip, (time.time() - start_time))
        )
    except JSONDecodeError:
        print("Request not completed. Failed JSON decoding.\n")


def proxy_job_execution(requests_number: int = 10):
    proxy_switcher = ProxySwitcher(PROXY_LIST, PORT_LIST)
    for _ in range(requests_number):
        proxy_switcher.set_proxy()
        check_ip()  # This is meant to be changed to your scrapping job or task that requires proxy-switching


if __name__ == "__main__":
    proxy_job_execution(NUM_TOTAL_REQUESTS)

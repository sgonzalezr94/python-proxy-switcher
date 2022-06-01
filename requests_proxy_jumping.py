from settings import IP_CHECKER_URL
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

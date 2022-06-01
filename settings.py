import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# This lists must be defined here, you can create a method to scrap available proxies over the web and then populate this constants with the data.
PROXY_LIST, PORT_LIST = ["80.48.119.28", "46.232.121.215"], ["8080", "80"]

IP_CHECKER_URL = "http://ip-api.com/json"

NUM_TOTAL_REQUESTS = 5

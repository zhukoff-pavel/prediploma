import json
import random

import requests
import time

prev_values = {   # Dict to avoid noise in data.
    1: {          # UID
        1: 0,     # CID: VALUE
        2: 1,
        3: 2,
        4: 3,
        5: 4,
    },
    2: {          # UID
        1: 0,     # CID: VALUE
        2: 1,
        3: 2,
        4: 3,
        5: 4,
    },
    3: {          # UID
        1: 0,     # CID: VALUE
        2: 1,
        3: 2,
        4: 3,
        5: 4,
    },
    4: {          # UID
        1: 0,     # CID: VALUE
        2: 1,
        3: 2,
        4: 3,
        5: 4,
    },
    5: {          # UID
        1: 0,     # CID: VALUE
        2: 1,
        3: 2,
        4: 3,
        5: 4,
    },
}

ID = random.randint(1, 5) # Random ID. Basicaly -- insert your own data (uuid?)

while True: # Spam with data entries to form continuous line. Each entry has data from 5 "sensors".
    payload = {
        "tstamp": time.time(),
        "data": []
    }
    for i in range(1, 6):
        new_d = prev_values[ID][i] + random.uniform(-1, 1)
        payload["data"].append(
            {
                "cid": i,
                "value": new_d
            }
        )
        prev_values[ID][i] = new_d
    r = requests.put(f"http://127.0.0.1:8000/id/{ID}", data=json.dumps(payload)) # Intended to use locally, so localhost is fine.

    time.sleep(1)

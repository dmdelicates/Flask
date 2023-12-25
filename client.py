from pprint import pprint

import requests

data = requests.post(
    "http://127.0.0.1:5000/adv/",
    json={"header": "sdfg", "description": "gfhj", "owner": "FlaskUser"},
)
print(data.status_code)
print(data.text)


# data = requests.get("http://127.0.0.1:5000/adv/FlaskUser")
# print(data.status_code)
# pprint(data.text)

# data = requests.delete("http://127.0.0.1:5000/adv/1")
# print(data.status_code)
# pprint(data.text)

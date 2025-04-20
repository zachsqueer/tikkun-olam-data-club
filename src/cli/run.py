import requests
from interfaces import google_auth
from pprint import pprint


BASE_URL = "https://sheets.googleapis.com/v4/spreadsheets"
ENDPOINTS = {
    "metadata": "",
    "batch_get": "values:batchGet",
    "batch_update": ":batchUpdate",
}

ID = "1dpW9eEg7dduk_7ztguU7NYbtqp44KiLgY_4zvHGBsTg"


def main():
    url = BASE_URL + "/" + ID + "/" + ENDPOINTS["batch_get"]

    creds = google_auth()

    headers = {"Authorization": f"Bearer {creds.token}"}

    everett = {"ranges": "garret"}

    response = requests.get(url, headers=headers, params=everett)
    data = response.json()

    pprint(data)


if __name__ == "__main__":
    main()

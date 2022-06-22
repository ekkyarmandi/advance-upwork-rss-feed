'''
Return available current earnings from UpWork in my Notion Database. Including updating it's convertion rates and available dates.
'''
from forex_python.converter import CurrencyRates
from credentials import NOTION_KEY
from datetime import datetime
import requests


def query(database_id, filter={}):
    api_url = f"https://api.notion.com/v1/databases/{database_id}/query"
    payload = {
        "filter": filter
    }
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + NOTION_KEY
    }
    resp = requests.post(api_url, json=payload, headers=headers)
    if resp.status_code == 200:
        return resp.json()

def query_earnings():

    def get_item_property(page,field_key):
        properties = page['properties'][field_key]
        type_ = properties.get('type')
        value = properties[type_]
        return value

    def convert_date(str):
        return datetime.strptime(str,"%Y-%m-%d")

    database_id = "db0f0eb7de894b0b978bf05802e45828"
    filter = {
        "and": [
            {
                "property": "💸 Withdrawn",
                "checkbox": {
                    "equals": False
                }
            },
            {
                "property": "Paid Status",
                "rich_text": {
                    "contains": "Paid"
                }
            }
        ]
    }
    output = query(database_id,filter)
    results = output['results']

    forex = CurrencyRates()
    idr_rate = forex.get_rate('USD','IDR')

    value = 0
    latest_dates = []
    for page in results:
        value += get_item_property(page,'Net Amount (USD)')
        paid_date = get_item_property(page,'Paid Arrived')
        paid_date = paid_date['date']['start']
        latest_dates.append(paid_date)

    avail_date=max(list(map(convert_date,latest_dates)))
    return dict(
        value_usd=value,
        value_idr=value*idr_rate,
        usd_idr=idr_rate,
        avail_date=avail_date.strftime("%d %b %Y")
    )

if __name__ == "__main__":

    results = query_earnings()
    print(results)
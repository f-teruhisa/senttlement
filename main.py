"""
requests: HTTP Clients for API request
datetime: Get today's date
"""
import datetime
import requests

URL = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json"

params = {
  "date": datetime.date.today(),
  "type": 2
}

res = requests.get(URL, params=params, verify=False)

print(res.text)

"""
requests: HTTP Clients for API request
datetime: Get today's date
"""
import datetime
import json
import requests

URL = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json"

params = {
  "date": datetime.date.today(),
  "type": 2
}

req = requests.get(URL, params=params, verify=True)

response_json = json.loads(req.text)
results = response_json["results"]

for result in results:
    # Guard empty documents data in response body
    if result['edinetCode'] is None:
        continue
    print(result['docID'], result['docDescription'],result['filerName'])

import requests
import datetime

url = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json"

params = {
  "date": datetime.date.today(),
  "type": 2
}

res = requests.get(url, params=params, verify=False)

print(res.text)

import requests
import json
from requests.auth import HTTPBasicAuth

url = "http://localhost:8080/api/v1/dags"
response = requests.get(url, auth=HTTPBasicAuth('airflow', 'airflow')).json()['dags']
result = {'dags': [], 'total_entries': 0}
dags = []

for i in response:
    if i['is_paused'] == False:
        dags.append(i)

result['dags'] = dags
result['total_entries'] = len(dags)

print(json.dumps(result, ensure_ascii=False, indent=3))
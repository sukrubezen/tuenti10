import requests

url = "steam-origin.contest.tuenti.net:9876/games/cat_fight/get_key"

payload = {}
headers = {
  'Host': 'pre.steam-origin.contest.tuenti.net'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

import requests
url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers={"Accept": "application/json"}) # This tells the server to send the plain text version not the html

#print(f"Your request to {url} came back w/ status code {response.status_code}")

#print(response.text)

data = response.json()
print(data)
print(data["joke"])
print(f"status: {data['status']}")
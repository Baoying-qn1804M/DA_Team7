import requests


url = "http://172.18.58.238/photography/"

r = requests.get(url)

print("Status code:")
print("\t *", r.status_code)

h = requests.head(url)
print("Header:")
print("**********")

for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

headers = {
    'User-Agent': "Mobile"
}

r = requests.get(url)

url2 = "http://172.18.58.238/photography/"
rh = requests.get(url2, headers=headers)
print(rh.text)

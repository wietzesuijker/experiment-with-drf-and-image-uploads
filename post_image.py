import requests
img = "./test.tiff"
files = {"raster": (img, open(img, "rb"))}
url = "http://127.0.0.1:8000/api/raster/"
headers = {"Authorization": "Token  bbc0d42ba52f25a672a784941c7b74ed7d0d6ca3"}
r = requests.post(url=url, headers=headers, files=files)
print(r.json())

import requests
from datetime import datetime
GRAPHID= ""
TOKEN = ""
USERNAME = ""
today = datetime.now()
pixela_endpoint = " https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph9",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"}
headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"


post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?"),

}
response = requests.post(url=pixel_endpoint, json=post_config, headers=headers)
print(response.text)
# i want to update the pixela data
put_pixela = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
put_config = {
    "quantity": "25"
}

#delete_pixela = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
#response = requests.delete(url=delete_pixela, headers=headers)

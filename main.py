import requests
from datetime import datetime
GRAPHID= "graph9"
TOKEN = "wlndfsedrgk09"
USERNAME = "boodi"
today = datetime.now()
pixela_endpoint = " https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
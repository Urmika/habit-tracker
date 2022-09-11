import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv('USERNAME')
TOKEN =  os.getenv('TOKEN')
GRAPH_ID=  os.getenv('GRAPH_ID')

today = datetime.now()
#today = datetime(year=2022,month=7, day=11)
formatted_date = today.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
colour_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
update_endpoint = f"{colour_endpoint}/{formatted_date}"
delete_endpoint = update_endpoint

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response = requests.post(url=pixela_endpoint, json= user_params)
# print(response.text)

graph_config ={
    "id": GRAPH_ID,
    "name": "rhodestracker",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

colour_config ={
    "date": formatted_date,
    "quantity": input("How would you rate your effort for today? ")
}
response = requests.post(url=colour_endpoint,headers=headers,json=colour_config)
print(response.text)

update_config ={
    "quantity" : "15"
}
# response = requests.put(url=update_endpoint,headers=headers,json=update_config)
# print(response.text)

# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)
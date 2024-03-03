import requests
import datetime as dt
BASE_URL = "https://pixe.la/v1"
USERNAME = "python1developer"
TOKEN = "6fa459ea-ee8a-3ca4-894e-db77e160355e" # Generate once by user
PURPLE_COLOR = "ajisai"
GRAPH_ID = "graph1"
header = {
    "X-USER-TOKEN": TOKEN
}
today = dt.datetime.now().strftime("%Y%m%d")
# --------------------------- CREATE USER ---------------------------
# create_user_param = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# create_user_response = requests.post(url=f"{PIXELA_URL}/users", json=create_user_param)
# print(create_user_response.text)
# {"message":"Success. Let's visit https://pixe.la/@python1developer , it is your profile page!","isSuccess":true}


# --------------------------- CREATE GRAPH ---------------------------
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Pages read",
#     "unit": "pages",
#     "type": "int",
#     "color": PURPLE_COLOR,
# }
# create_graph_response = requests.post(url=f"{BASE_URL}/users/{USERNAME}/graphs",
#                                       headers=header,
#                                       json=graph_params)
# print(create_graph_response.text)
# https://pixe.la/v1/users/python1developer/graphs/graph1.html

# --------------------------- POSTING THE PIXEL ---------------------------
pages = int(input("How many page you read today?"))
pix_params = {
    "date": today,
    "quantity": pages,
}
add_pixel_response = requests.post(url=f"{BASE_URL}/users/{USERNAME}/graphs/{GRAPH_ID}",
                                   headers=header,
                                   json=pix_params)
print(add_pixel_response.text)

# --------------------------- EDIT THE PIXEL ---------------------------
# pix_params = {
#     "quantity": "10",
# }
# edit_pixel_response = requests.put(url=f"{BASE_URL}/users/{USERNAME}/graphs/{GRAPH_ID}/{today}",
#                                    headers=header,
#                                    json=pix_params)
# print(edit_pixel_response.text)

# --------------------------- DELETE THE PIXEL ---------------------------
# delete_pixel_response = requests.delete(url=f"{BASE_URL}/users/{USERNAME}/graphs/{GRAPH_ID}/{today}",
#                                    headers=header)
# print(delete_pixel_response.text)
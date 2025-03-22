import requests

# Secret Token
TOKEN = ""
USERNAME = ""
GRAPHNAME = ""

PIXELA_URL_USER_ACCOUNT = "https://pixe.la/v1/users"
PIXELA_URL_GRAPH_DEFINITION = f"https://pixe.la/v1/users/{USERNAME}/graphs"
PIXELA_URL_GRAPH_VALUE = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHNAME}"


parameters_user_account = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

parameters_graph_definition = {
    "id": "walking-graph",
    "name": "walking-graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

parameters_graph_value = {
    "date": "20230322",
    "quantity": "3.19",
}

# response_user_account = requests.post(url=PIXELA_URL_USER_ACCOUNT, json=parameters_user_account)
# print(response_user_account.text)

# response_graph_definition = requests.post(url=PIXELA_URL_GRAPH_DEFINITION,
#                                           json=parameters_graph_definition,
#                                           headers=headers)
# print(response_graph_definition.text)

# response_graph_value = requests.post(url=PIXELA_URL_GRAPH_VALUE, json=parameters_graph_value, headers=headers)
# print(response_graph_value.text)

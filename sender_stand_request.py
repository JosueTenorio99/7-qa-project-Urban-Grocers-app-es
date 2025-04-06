import configuration
import requests
import data

#Función para crear un nuevo usuario y obtener el auth Token
def get_new_user_token():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=data.user_body.copy())
    return response.json()["authToken"]

def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body, headers=headers)


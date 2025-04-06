import data
import sender_stand_request

# Función para obtener un nombre de kit personalizado
def get_kit_body(name):
    new_kit = data.kit_body.copy()
    new_kit["name"] = name
    return new_kit

# Prueba positiva: código esperado 201
def positive_assert(name):
    kit_body = get_kit_body(name)
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]
    print(response.status_code)
    print(response.json())

# Prueba negativa: código esperado 400
def negative_assert_code_400(kit_body_name):
    kit_body = get_kit_body(kit_body_name)
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400
    print(response.status_code)


# Prueba negativa con el cuerpo del kit vacío: código esperado 400
def kit_body_empty():
    kit_body = {}  # no contiene el campo "name"
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400
    print(response.status_code)
    print(response.json())

# ✅ PRUEBAS

#Prueba 1: Aprobada. Code: 201
def test_kit_name_1_character():
    positive_assert("aa")

#Prueba 2: Aprobada. Code: 201
def test_kit_name_511_characters():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Prueba 3: No aprobada. Code: 201
def test_kit_name_empty():
    negative_assert_code_400("")

#Prueba 4: No aprobada. Code: 201
def test_kit_name_512_characters():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba 5: Aprobada. Code: 201
def test_kit_name_special_characters():
    positive_assert("№%@,.")

#Prueba 6: Aprobada. Code: 201
def test_kit_name_with_spaces():
    positive_assert(" A Aaa ")

#Prueba 7: Aprobada. Code: 201
def test_kit_name_with_numbers():
    positive_assert("123")

#Prueba 8: No aprobada. Code: 500
def test_kit_name_missing_parameter():
    kit_body_empty()


#Prueba 9: No aprobada. Code: 201
def test_kit_name_number_instead_of_string():
    negative_assert_code_400(231)

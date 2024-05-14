import json

import allure
from jsonschema import validate

from utils.helpers import api_get_method
from utils.util import load_schema


def test_validate_get_method():
    '''GIVEN'''
    name = "bob"
    api_url = '1399'

    '''WHEN'''
    with allure.step('Выполнить метод получения данных питомца по id'):
        response = api_get_method(api_url)
        response_body = response.json()
    with allure.step('Поместить эталонную схему в переменную'):
        schema = load_schema("post_method.json")

    '''THEN'''
    with allure.step('Сравнить статус код ответа'):
        assert response.status_code == 200
    with allure.step('Проверить имя полученного питомца'):
        assert response_body['name'] == name
    with allure.step('Сравнить структуру ответа с эталонной структурой'):
        with open(schema) as file:
            schema = json.load(file)
            validate(response_body, schema=schema)

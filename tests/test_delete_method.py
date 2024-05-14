import json

import allure
from jsonschema import validate

from utils.helpers import api_delete_method
from utils.util import load_schema


def test_unsuccessful_delete_method():
    '''GIVEN'''
    api_url = "8888"

    '''WHEN'''
    with allure.step('Выполнить метод удаления данных несуществующего питомца'):
        response = api_delete_method(api_url)

    '''THEN'''
    with allure.step('Сравнить статус код ответа'):
        assert response.status_code == 404


def test_successful_delete_method():
    '''GIVEN'''
    api_url = "199"

    '''WHEN'''
    with allure.step('Выполнить метод удаления данных существующего питомца'):
        response = api_delete_method(api_url)
        response_body = response.json()
    with allure.step('Поместить эталонную схему в переменную'):
        schema = load_schema("delete_method.json")

    '''THEN'''
    with allure.step('Сравнить статус код ответа'):
        assert response.status_code == 200
    with allure.step('Сравнить структуру ответа с эталонной структурой'):
        with open(schema) as file:
            schema = json.load(file)
            validate(response_body, schema=schema)

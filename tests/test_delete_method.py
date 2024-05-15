import json

import allure
from jsonschema import validate

from utils.helpers import api_delete_method
from utils.util import load_schema


def test_unsuccessful_delete_method(api_url, headers):
    '''GIVEN'''
    for_api_url = "8888"
    body = "[]"

    '''WHEN'''
    with allure.step('Выполнить метод удаления данных несуществующего питомца'):
        response = api_delete_method(api_url, for_api_url, headers)

    '''THEN'''
    with allure.step('Сравнить статус код ответа'):
        assert response.status_code == 404
    with allure.step('Сравнить url запроса с url из ответа'):
        assert response.url == f"{api_url}{for_api_url}"


def test_successful_delete_method(api_url, headers):
    '''GIVEN'''
    for_api_url = "199"

    '''WHEN'''
    with allure.step('Выполнить метод удаления данных существующего питомца'):
        response = api_delete_method(api_url, for_api_url, headers)
        response_body = response.json()
    with allure.step('Поместить эталонную схему в переменную'):
        schema = load_schema("delete_method.json")

    '''THEN'''
    with allure.step('Сравнить статус код ответа'):
        assert response.status_code == 200
    with allure.step('Сравнить айди удаляемого значения из запроса с айди из ответа'):
        assert response_body["message"] == for_api_url
    with allure.step('Сравнить структуру ответа с эталонной структурой'):
        with open(schema) as file:
            schema = json.load(file)
            validate(response_body, schema=schema)

import json

import allure
from jsonschema import validate

from utils.helpers import api_request
from utils.util import load_schema


def test_validate_put_method(api_url, headers):
    '''GIVEN'''
    name = "bobr kurva"

    '''WHEN'''
    with allure.step('Выполнить метод редактирования данных существующего питомца'):
        response = api_request(api_url=api_url, headers=headers)
        response_body = response.json()
    with allure.step('Поместить эталонную схему в переменную'):
        schema = load_schema("post_method.json")

    '''THEN'''
    with allure.step('Сравнить статус код ответа'):
        assert response.status_code == 200
    with allure.step('Проверить что имя питомца изменилось на новое'):
        assert response_body["name"] == name
    with allure.step('Сравнить структуру ответа с эталонной структурой'):
        with open(schema) as file:
            schema = json.load(file)
            validate(response_body, schema=schema)

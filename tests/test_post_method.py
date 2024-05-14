import json

import allure
from jsonschema import validate

from utils.helpers import api_post_method
from utils.util import load_schema


def test_validate_post_method():
    '''WHEN'''
    with allure.step('Выполнить метод создания нового питомца'):
        response = api_post_method()
        response_body = response.json()
    with allure.step('Поместить эталонную схему в переменную'):
        schema = load_schema("post_method.json")

    '''THEN'''
    with allure.step('Сравнить статус код ответа'):
        assert response.status_code == 200
    with allure.step('Сравнить структуру ответа с эталонной структурой'):
        with open(schema) as file:
            schema = json.load(file)
            validate(response_body, schema=schema)

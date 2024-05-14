import json
import logging

from allure_commons.types import AttachmentType
import allure
import requests

url = "https://petstore.swagger.io/v2/pet/"
headers = {"content-type": "application/json"}
data_post = {
    "id": 199,
    "category": {
        "id": 199,
        "name": "bob"
    },
    "name": "bob",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 199,
            "name": "bob"
        }
    ],
    "status": "available"
}
data_put = {
    "id": 199,
    "category": {
        "id": 199,
        "name": "bob"
    },
    "name": "bobr kurva",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 199,
            "name": "bob"
        }
    ],
    "status": "available"
}


def api_get_method(api_url):
    with allure.step('API get method'):
        response = requests.get(url=url + api_url, headers=headers)
        response_logging(response)
        response_attaching(response)

        return response


def api_post_method():
    with allure.step('API post method'):
        json_data = json.dumps(data_post)
        response = requests.post(url=url, data=json_data, headers=headers)
        response_logging(response)
        response_attaching(response)

        return response


def api_put_method():
    with allure.step('API put method'):
        json_data = json.dumps(data_put)
        response = requests.put(url=url, data=json_data, headers=headers)
        response_logging(response)
        response_attaching(response)

        return response


def api_delete_method(api_url):
    with allure.step('API delete method'):
        response = requests.delete(url=url + api_url, headers=headers)

    return response


def response_attaching(response_body):
    allure.attach(
        body=json.dumps(response_body.json(), indent=4, ensure_ascii=True),
        name="Response", attachment_type=AttachmentType.JSON, extension="json"
    )


def response_logging(response_body):
    logging.info("Request: " + response_body.request.url)
    if response_body.request.body:
        logging.info("INFO Request body: " + response_body.request.body)
    logging.info("Request headers: " + str(response_body.request.headers))
    logging.info("Response code " + str(response_body.status_code))

import json
import logging

from allure_commons.types import AttachmentType
import allure
import requests

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


def api_request(api_url, headers, method='put', for_api_url=None):
    with allure.step(f'API {method} method'):

        if method == 'get':
            response = requests.get(url=api_url + for_api_url, headers=headers)
        elif method == 'post':
            json_data = json.dumps(data_post)
            response = requests.post(url=api_url, data=json_data, headers=headers)
        elif method == 'put':
            json_data = json.dumps(data_put)
            response = requests.put(url=api_url, data=json_data, headers=headers)
        elif method == 'delete':
            response = requests.delete(url=api_url + for_api_url, headers=headers)
        else:
            raise ValueError(f"Unsupported method: {method}")

        response_logging(response)
        response_attaching(response)
        return response


def is_json(response_body):
    try:
        response_body.json()
        return True
    except ValueError:
        return False


def response_attaching(response_body):
    allure.attach(
        body=response_body.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response_body.request.body:
        allure.attach(
            body=response_body.request.body.decode() if isinstance(response_body.request.body,
                                                                   bytes) else response_body.request.body,
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )

    if is_json(response_body):
        response_json = response_body.json()
        allure.attach(
            body=json.dumps(response_json, indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json"
        )
    else:
        allure.attach(
            body=response_body.text,
            name="Response",
            attachment_type=AttachmentType.TEXT,
        )


def response_logging(response_body):
    logging.info("Request: " + response_body.request.url)
    if response_body.request.body:
        logging.info("INFO Request body: " + str(response_body.request.body))
    logging.info("Request headers: " + str(response_body.request.headers))
    logging.info("Response code: " + str(response_body.status_code))

    if is_json(response_body):
        response_json = response_body.json()
        logging.info("Response: " + json.dumps(response_json, indent=4))
    else:
        logging.info("Response: " + response_body.text)

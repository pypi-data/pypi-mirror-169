import json

import requests


from ..utils import confirm_signature, generate_signature


def make_payment(invoice: dict, slickpay_api_url="https://slickpay.azimutbscenter.com/api/slickapiv1/transfer") -> requests.Response:
    headers = {"Accept": "application/json"}
    print('befor response', invoice)

    response = requests.post("https://slickpay.azimutbscenter.com/api/slickapiv1/transfer", json=invoice, headers=headers)
    print('after response', response)
    return response


def send_fake_payment_confirmation(body: dict, secret_key: str, request_url: str):
    encoded_body = json.dumps(body).encode()
    encoded_key = secret_key.encode()

    signature = generate_signature(encoded_body, encoded_key)

    headers = {
        "Signature": signature,
        "Accept": "application/json",
    }

    requests.post(request_url, headers=headers, json=body)


class PaymentManager:
    def __init__(self, api_url) -> None:
        self._api_url = api_url

    def make_payment(self, invoice: dict) -> requests.Response:
        return make_payment(invoice, self._api_url)

    def make_confirmation(self, body, request_signature):
        return confirm_signature(body, request_signature)



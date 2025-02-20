# Copyright 2025 Webullpay
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from webullpaysdkcore.client import ApiClient
from webullpaysdkcore.exception.exceptions import ServerException
from webullpaysdktrade.request.palce_order_request import PlaceOrderRequest


optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
api_client = ApiClient(your_app_key, your_app_secret)
crypto_order = {
    "account_id": "abc123",
    "crypto_order": {
        "request_id": "A0191646207512192E",
        "instrument_id": "913256409",
        "side": "BUY",
        "tif": "IOC",
        "order_type": "MKT",
        "qty": "1",
        "entrust_type": "QTY"
    }
}


class TestOrderOperation(unittest.TestCase):
    def test_order(self):
        request = PlaceOrderRequest()
        request.set_endpoint(optional_api_endpoint)
        request.set_account_id(crypto_order['account_id'])
        request.set_request_id(crypto_order['crypto_order']['request_id'])
        request.set_side(crypto_order['crypto_order']['side'])
        request.set_tif(crypto_order['crypto_order']['tif'])
        request.set_instrument_id(crypto_order['crypto_order']['instrument_id'])
        request.set_order_type(crypto_order['crypto_order']['order_type'])
        request.set_qty(crypto_order['crypto_order']['qty'])
        request.set_entrust_type(crypto_order['crypto_order']['entrust_type'])
        post_body = request.get_body_params()
        print(post_body)
        params = request.get_query_params()
        print(params)
        try:
            response = api_client.get_response(request)
            print(response.json())

        except ServerException as se:
            print(se.get_error_code(), ":", se.get_error_msg())
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
import uuid

from webullpaysdkcore.client import ApiClient

from webullpaysdktrade.trade.order_operation import OrderOperation

optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
api_client = ApiClient(your_app_key, your_app_secret)
api_client.add_endpoint('us', optional_api_endpoint)


class TestorderOperation(unittest.TestCase):
    def test_order_operation(self):
        order_operation = OrderOperation(api_client)
        request_id = uuid.uuid4().hex
        client_order_id = ""
        crypto_order = {
            "account_id": "abc123",
            "crypto_order": {
                "request_id": request_id,
                "instrument_id": "913256409",
                "order_type": "MKT",
                "tif": "IOC",
                "side": "BUY",
                "entrust_type": "QTY",
                "qty": "1",
            }
        }

        res = order_operation.place_order(account_id, **crypto_order['crypto_order'])
        if res.status_code == 200:
            print('place order status:', res.json())
            client_order_id = res.json()[client_order_id]
        res = order_operation.query_order_detail(account_id, client_order_id)
        if res.status_code == 200:
            print('order details:', res.json())

        res = order_operation.list_open_orders(account_id)
        if res.status_code == 200:
            print('open orders:', res.json())

        res = order_operation.list_today_orders(account_id)
        if res.status_code == 200:
            print('today orders:', res.json())

        cancel_client_order_id = client_order_id
        res = order_operation.cancel_order(account_id, cancel_client_order_id)
        if res.status_code == 200:
            print('cancel order response:', res.json())

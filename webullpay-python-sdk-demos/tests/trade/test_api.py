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
from webullpaysdkmdata.common.category import Category
from webullpaysdktrade.api import API
from webullpaysdktrade.common.instrument_type import InstrumentType

# optional_api_endpoint = "<api_endpoint>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
account_id = "<your_account_id>"
# 'us'
region_id = "<region_id>"
api_client = ApiClient(your_app_key, your_app_secret, region_id)
# api_client.add_endpoint(region_id, optional_api_endpoint)


class TestApi(unittest.TestCase):
    def test_api(self):
        api = API(api_client)
        res = api.instrument.get_instrument('BTCUSD', 'CRYPTO')
        if res.status_code == 200:
            print(res.json())
        res = api.instrument.get_instrument('ETHUSD', 'CRYPTO')
        if res.status_code == 200:
            print(res.json())
        res = api.instrument.get_instrument('PEPEUSD', Category.CRYPTO.name)
        if res.status_code == 200:
            print(res.json())
        res = api.market_data.get_snapshot('ETHUSD', 'CRYPTO')
        if res.status_code == 200:
            print('crypto quote:', res.json())
        res = api.market_data.get_history_bar('BTCUSD', 'CRYPTO', 'M1')
        if res.status_code == 200:
            print('crypto history bar:', res.json())

        res = api.trade_instrument.get_tradable_instruments(account_id)
        if res.status_code == 200:
            print('tradable instruments:', res.json())
        res = api.account.get_app_subscriptions()
        if res.status_code == 200:
            print('app subscriptions:', res.json())
        res = api.account.get_account_profile(account_id)
        if res.status_code == 200:
            print('account profile:', res.json())
        res = api.account.get_account_position(account_id)
        if res.status_code == 200:
            print('account position:', res.json())
        res = api.account.get_account_balance(account_id)
        if res.status_code == 200:
            print('account balance:', res.json())

        client_order_id = ""
        request_id = uuid.uuid4().hex
        print('request id:', request_id)
        crypto_order = {
            "account_id": account_id,
            "crypto_order": {
                "request_id": request_id,
                "instrument_id": "913256135",
                "side": "BUY",
                "tif": "IOC",
                "order_type": "MKT",
                "entrust_type": "QTY",
                "qty": "1"
            }
        }
        """
        LIMIT crypto_order
        crypto_order = {
            "account_id": account_id,
            "crypto_order": {
                "request_id": request_id,
                "instrument_id": "913256135",
                "side": "BUY",
                "tif": "DAY",
                "order_type": "LIMIT",
                "limit_price": "93850.000",
                "entrust_type": "QTY",
                "qty": "1",
            }
        }
        """
        """
        STOP_LOSS_LIMIT crypto_order
        crypto_order = {
            "account_id": account_id,
            "crypto_order": {
                "request_id": request_id,
                "instrument_id": "913256135",
                "side": "BUY",
                "tif": "DAY",
                "order_type": "STP_LMT",
                "stop_price": "98500.000",
                "limit_price": "98500.100",
                "entrust_type": "QTY"
                "qty": "1"
            }
        }
        """

        res = api.order.place_order(crypto_order['account_id'], **crypto_order['crypto_order'])
        if res.status_code == 200:
            print('place order res:', res.json())
            client_order_id = res.json()['client_order_id']
        res = api.order.list_open_orders(account_id, page_size=20)
        if res.status_code == 200:
            print('open orders:', res.json())
        res = api.order.list_today_orders(account_id, page_size=20)
        if res.status_code == 200:
            print('today orders', res.json())
        res = api.order.query_order_detail(account_id, client_order_id)
        if res.status_code == 200:
            print('order detail:', res.json())
        res = api.order.cancel_order(account_id, client_order_id)
        if res.status_code == 200:
            print('cancel order status:', res.json())

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
from webullpaysdktrade.request.get_tradable_instruments_request import TradableInstrumentRequest

optional_api_endpoint = "<api_endpoint>"
account_id = "<account_id>"
your_app_key = "<your_app_key>"
your_app_secret = "<your_app_secret>"
api_client = ApiClient(your_app_key, your_app_secret)


class TesttradableInstruments(unittest.TestCase):

    def test_tradable_instruments(self):
        request = TradableInstrumentRequest()
        request.set_account_id(account_id)
        try:
            response = api_client.get_response(request)
            print(response.json())
        except ServerException as se:
            print(se.get_error_code(), ":", se.get_error_msg())

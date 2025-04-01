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

import logging
import unittest

from webullpaysdkmdata.common.category import Category
from webullpaysdkmdata.common.subscribe_type import SubscribeType
from webullpaysdkmdata.quotes.subscribe.default_client import DefaultQuotesClient

your_app_key = "</your_app_key>"
your_app_secret = "</your_app_secret>"
optional_quotes_endpoint = "</optional_quotes_endpoint>"


class TestDefaultQuotesClient(unittest.TestCase):

    def test_default_quotes_client(self):
        def pt_logs(client, userdata, level, buf):
            print("userdata:%s, level:%s, buf:%s" % (userdata, level, buf))

        def on_quotes_message(client, userdata, message):
            print("Received message userdata: %s,%s'" % (userdata, message))

        client = DefaultQuotesClient(your_app_key, your_app_secret, 'us', optional_quotes_endpoint)
        client.init_default_settings('BTCUSD', Category.CRYPTO.name, SubscribeType.SNAPSHOT.name)
        # client.on_log = pt_logs
        client.on_quotes_message = on_quotes_message
        client.connect_and_loop_forever()

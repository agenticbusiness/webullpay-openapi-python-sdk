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

# coding=utf-8

import time
import unittest

from webullpaysdkcore.request import ApiRequest
from webullpaysdkquotescore.exceptions import ExitedException
from webullpaysdkquotescore.quotes_client import QuotesClient

PRE_HOST = "<quotes_endpoint>"
PRE_OPENAPI_ENDPOINT = "<api_endpoint>"


class TestQuotesClient(unittest.TestCase):

    def test_connection(self):
        client = QuotesClient("<your_app_key>",
                              "<your_app_secret>")

        def _refresh_token_func(client, api_client):
            request = ApiRequest("/market-data/streaming/token")
            request.set_endpoint(PRE_OPENAPI_ENDPOINT)
            response = api_client.get_response(request)
            return response.json()['token']

        def _on_quotes_subscribe_func(client, api_client, quotes_token):
            print(
                "intention to invoke disconnect method and not do quotes subscribe, api_client:%s, quotes_token:%s" % (
                    api_client, quotes_token))
            client.disconnect()
            print("raise ExitedException to stop processing")
            raise ExitedException()

        client.on_refresh_token = _refresh_token_func
        client.on_quotes_subscribe = _on_quotes_subscribe_func
        try:
            client.connect_and_loop_forever(PRE_HOST)
        except:
            pass

    def test_quotes_subscribe(self):
        client = QuotesClient("<your_app_key>",
                              "<your_app_secret>")

        def _refresh_token_func(client, api_client):
            request = ApiRequest("/market-data/streaming/token")
            request.set_endpoint(PRE_OPENAPI_ENDPOINT)
            response = api_client.get_response(request)
            return response.json()['token']

        def _quotes_subscribe_func(client, api_client, quotes_token):
            request = ApiRequest(
                "/market-data/streaming/subscribe", body_params={})
            request.set_endpoint(PRE_OPENAPI_ENDPOINT)
            request.add_body_params('token', quotes_token)
            request.add_body_params('symbols', ["BTCUSD"])
            request.add_body_params('category', "CRYPTO")
            request.add_body_params('sub_types', ["BASIC_QUOTE", "SNAPSHOT"])
            response = api_client.get_response(request)
            return response.status_code == 200

        def _on_quotes_message_func(client, topic, data):
            print("just call disconnect in sub thread")
            client.disconnect()
            print("just call loop stop in sub thread")
            client.loop_stop()

        def _on_log_func(client, userdata, level, buf):
            print("userdata:%s, level:%s, buf:%s" % (userdata, level, buf))

        client.on_log = _on_log_func
        client.on_refresh_token = _refresh_token_func
        client.on_quotes_subscribe = _quotes_subscribe_func
        client.on_quotes_message = _on_quotes_message_func

        client.connect_and_loop_start(PRE_HOST)
        print("main thread will start sleeping")
        time.sleep(15)
        print("main thread done")

    def test_quotes_message(self):
        client = QuotesClient("<your_app_key>",
                              "<your_app_secret>")

        def _refresh_token_func(client, api_client):
            request = ApiRequest("/market-data/streaming/token")
            request.set_endpoint(PRE_OPENAPI_ENDPOINT)
            response = api_client.get_response(request)
            return response.json()['token']

        def _quotes_subscribe_func(client, api_client, quotes_token):
            request = ApiRequest(
                "/market-data/streaming/subscribe", body_params={})
            request.set_endpoint(PRE_OPENAPI_ENDPOINT)
            request.add_body_params('token', quotes_token)
            request.add_body_params('symbols', ["BTCUSD"])
            request.add_body_params('category', "CRYPTO")
            request.add_body_params('sub_types', ["BASIC_QUOTE", "SNAPSHOT"])
            response = api_client.get_response(request)
            return response.status_code == 200

        def _on_log_func(client, userdata, level, buf):
            print("userdata:%s, level:%s, buf:%s" % (userdata, level, buf))

        client.on_log = _on_log_func

        def _on_quotes_message_func(client, topic, data):
            print("topic received=", topic, "data received=", data)

        client._on_log = _on_log_func
        client.on_refresh_token = _refresh_token_func
        client.on_quotes_subscribe = _quotes_subscribe_func
        client.on_quotes_message = _on_quotes_message_func

        client.connect_and_loop_start(PRE_HOST)
        print("main thread will start sleeping")
        time.sleep(15)
        print("call loop stop in main thread")
        client.loop_stop()
        print("main thread done")

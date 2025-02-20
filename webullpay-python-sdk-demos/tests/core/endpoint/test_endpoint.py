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
from webullpaysdkcore.common import api_type
from webullpaysdkcore.endpoint.default_endpoint_resolver import DefaultEndpointResolver
from webullpaysdkcore.endpoint.resolver_endpoint_request import ResolveEndpointRequest
from webullpaysdkmdata.request.get_instruments_request import GetInstrumentsRequest

# 'us'
region_id = '<region_id>'


class TestEndpoint(unittest.TestCase):

    def test_endpoint(self):
        """
            Set through ApiClient and take effect globally. The sample code is as follows.
        """
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>", region_id=region_id)

        client.add_endpoint("us", "<api_endpoint>")
        request = GetInstrumentsRequest()
        request.set_category("CRYPTO")
        request.set_symbols("BTCUSD")
        client.get_response(request)

    def test_endpoint_by_request(self):
        """
            Set by Request, and it only takes effect for the current Request. The sample code is as follows.
        """
        client = ApiClient(app_key="<your_app_key>", app_secret="<your_app_secret>")
        request = GetInstrumentsRequest()
        request.set_category("CRYPTO")
        request.set_symbols("BTCUSD")
        request.set_endpoint("<api_endpoint>")
        client.get_response(request)

    def test_quotes_endpoint(self):
        """
            Set by Request, and it only takes effect for the current Request. The sample code is as follows.
        """
        resolver = DefaultEndpointResolver(self)
        _region_id = 'us'
        endpoint_request = ResolveEndpointRequest(_region_id, api_type.QUOTES)
        endpoint = resolver.resolve(endpoint_request)
        self.assertEqual(endpoint, '')

    def test_api_endpoint(self):
        """
            Set by Request, and it only takes effect for the current Request. The sample code is as follows.
        """
        resolver = DefaultEndpointResolver(self)
        _region_id = 'us'
        endpoint_request = ResolveEndpointRequest(_region_id)
        endpoint = resolver.resolve(endpoint_request)
        self.assertEqual(endpoint, '')

    def test_event_endpoint(self):
        resolver = DefaultEndpointResolver(self)
        _region_id = 'us'
        endpoint_request = ResolveEndpointRequest(_region_id, api_type.EVENTS)
        endpoint = resolver.resolve(endpoint_request)
        self.assertEqual(endpoint, '')

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
from webullpaysdkcore.client import ApiClient
from webullpaysdkmdata.common.category import Category
from webullpaysdkmdata.request.get_snapshot_request import GetSnapshotRequest
from webullpaysdkmdata.request.get_quotes_request import GetQuotesRequest


if __name__ == '__main__':
    your_app_key = "<your_app_key>"
    your_app_secret = "<your_app_secret>"
    # 'us'
    region_id = '<region_id>'

    optional_api_endpoint = "<api_endpoint>"
    api_client = ApiClient(your_app_key, your_app_secret, region_id)
    request = GetSnapshotRequest()
    request.set_endpoint(optional_api_endpoint)
    request.set_category(Category.CRYPTO.name)
    request.set_symbols("BTCSUD")
    response = api_client.get_response(request)
    for quote_data in response.json():
        for key in quote_data.keys():
            print(key, quote_data[key], type(quote_data[key]), sep="|")
        print("-----------------------------------------")

    request = GetQuotesRequest()
    request.set_endpoint(optional_api_endpoint)
    request.set_category(Category.CRYPTO.name)
    request.set_symbol("BTCSUD")
    response = api_client.get_response(request)
    print(response.json())

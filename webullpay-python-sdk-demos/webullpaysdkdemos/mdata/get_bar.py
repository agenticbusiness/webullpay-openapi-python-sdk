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
from webullpaysdkmdata.common.timespan import Timespan
from webullpaysdkmdata.request.get_historical_bars_request import GetHistoricalBarsRequest


if __name__ == '__main__':
    your_app_key = "<your_app_key>"
    your_app_secret = "<your_app_secret>"
    # 'us'
    region_id = '<region_id>'

    # optional_api_endpoint = "<api_endpoint>"
    api_client = ApiClient(your_app_key, your_app_secret, region_id)
    request = GetHistoricalBarsRequest()
    # request.set_endpoint(optional_api_endpoint)
    request.set_category(Category.CRYPTO.name)
    request.set_symbol("BTCSUD")
    request.set_count(1440)
    request.set_timespan(Timespan.M1.name)
    response = api_client.get_response(request)
    print(response.json())

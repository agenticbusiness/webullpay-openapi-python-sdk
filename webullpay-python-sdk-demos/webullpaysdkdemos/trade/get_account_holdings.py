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

from webullpaysdktrade.trade.account_info import Account
from webullpaysdkcore.client import ApiClient


def print_holdings(holdings):
    if holdings:
        last_instrument_id = None
        for holding in holdings:
            last_instrument_id = holding['instrument_id']
            print(last_instrument_id)
            print(holding['instrument'])
            print(holding['instrument_type'])
            print(holding['quantity'])
            print(holding['total_cost'])
            print(holding['market_value'])
            print(holding['unrealized_profit_loss'])
            print(holding['unrealized_profit_loss_rate'])
        return last_instrument_id
    else:
        return None


if __name__ == '__main__':
    your_app_key = "<your_app_key>"
    your_app_secret = "<your_app_secret>"
    # 'us'
    region_id = 'us'
    api_client = ApiClient(your_app_key, your_app_secret, region_id)

    account_info = Account(api_client)
    response = account_info.get_app_subscriptions()
    profile_data = response.json()
    print(profile_data[0]['subscription_id'])
    print(profile_data[0]['account_id'])
    print(profile_data[0]['account_number'])

    account_id = profile_data[0]['account_id']
    response = account_info.get_account_position(account_id)
    account_positions = response.json()
    print(account_positions)

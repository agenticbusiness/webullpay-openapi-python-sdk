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

from webullpaysdkmdata.common.category import Category
from webullpaysdkmdata.common.subscribe_type import SubscribeType
from webullpaysdkmdata.quotes.subscribe.default_client import DefaultQuotesClient

if __name__ == '__main__':
    your_app_key = "<your_app_key>"
    your_app_secret = "<your_app_secret>"
    # 'us'
    region_id = '<region_id>'
    # not necessary in production env
    optional_quotes_grpc_endpoint = "<grpc_api_endpoint>"
    quotes_client = DefaultQuotesClient(
        your_app_key, your_app_secret, region_id)
    quotes_client.init_default_settings(["BTCUSD", "ETHUSD"], Category.CRYPTO.name, [
        SubscribeType.QUOTE.name, SubscribeType.SNAPSHOT.name])


    def my_quotes_message_func(client, topic, quotes):
        print("topic:%s, quotes:%s" % (topic, quotes))


    def my_subscribe_success_func(client, api_client, token):
        print("subscribe success with token:%s" % token)


    # set quotes receiving callback func
    quotes_client.on_quotes_message = my_quotes_message_func
    # set subscribe success callback func
    quotes_client.on_subscribe_success = my_subscribe_success_func
    # not necessary in production env
    optional_quotes_host = "<quotes_endpoint>"
    # the sync mode, blocking in current thread
    quotes_client.connect_and_loop_forever()

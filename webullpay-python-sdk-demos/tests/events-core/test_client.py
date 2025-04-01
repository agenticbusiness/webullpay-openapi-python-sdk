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

import logging
import unittest
from webullpaysdktradeeventscore.events_client import EventsClient
from webullpaysdkcore.retry.retry_policy import NO_RETRY_POLICY, RetryPolicy
from webullpaysdkcore.retry.retry_condition import MaxRetryTimesCondition
from webullpaysdkcore.retry.backoff_strategy import FixedDelayStrategy, NoDelayStrategy
from webullpaysdktradeeventscore.default_retry_policy import DefaultSubscribeRetryPolicy
from unittest.mock import patch

PRE_HOST = "</event_api_endpoint>"


class TestClient(unittest.TestCase):

    def test_error_appkey(self):
        client = EventsClient("app_key_mocked", "app_secret_mocked", host=PRE_HOST, retry_policy=NO_RETRY_POLICY)
        client.on_log = self._on_log
        try:
            client.do_subscribe(["<your_account_id>"])
        except:
            pass

    def test_error_appkey_and_retry(self):
        retry_policy = RetryPolicy(MaxRetryTimesCondition(3), FixedDelayStrategy(1000))
        client = EventsClient("app_key_mocked", "app_secret_mocked", host=PRE_HOST, retry_policy=retry_policy)
        client.on_log = self._on_log
        try:
            client.do_subscribe(["<your_account_id>"])
        except:
            pass

    def test_error_accounts(self):
        client = EventsClient("<your_app_key>", "app_secret_mocked", host=PRE_HOST)
        client.enable_logger()
        try:
            client.do_subscribe(["account_mocked"])
        except:
            pass
        try:
            client.do_subscribe("invalid_account_0,account_1")
        except:
            pass
        try:
            client.do_subscribe([])
        except:
            pass

    @patch("webullpaysdkcore.utils.common.get_uuid")
    def test_replay_connection(self, mock_get_uuid):
        mock_get_uuid.return_value = "the_same_nonce_value"
        retry_policy = RetryPolicy(MaxRetryTimesCondition(10), NoDelayStrategy())
        client = EventsClient("<your_app_key>", "app_secret_mocked", host=PRE_HOST, retry_policy=retry_policy)
        client.on_log = self._on_log
        try:
            client.do_subscribe(["account_mocked"])
        except:
            pass

    def test_normal(self):
        client = EventsClient("<your_app_key>", "<your_app_secret>", host=PRE_HOST)
        client.on_log = self._on_log
        client.do_subscribe(["<your_account_id>"])

    @staticmethod
    def _on_log(level, log_content):
        print(logging.getLevelName(level), log_content)

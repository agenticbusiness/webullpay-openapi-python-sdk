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
from webullpaysdkcore.utils import common
from webullpaysdkmdata.common.category import Category

class TestCategory(unittest.TestCase):
    def test_access(self):
        self.assertNotEqual(Category.CRYPTO, "CRYPTO")
        self.assertEqual(Category.CRYPTO.name, "CRYPTO")
        self.assertEqual(Category.CRYPTO, Category.from_string("CRYPTO"))
        try:
            Category.from_string("Unknown Category")
        except ValueError as ve:
            print(ve)
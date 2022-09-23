import unittest
import os
from app.simple_transaction import simple_transaction


class MyTestCase(unittest.TestCase):
    def test_simple_transaction(self):
        '''

        :return:
        '''


        blockery_api_key = os.environ['BLOCKERY_API_KEY']
        blockery_url = "https://app-stage.blockery.io"
        receive_address = 'addr_test1qrpzs98ufjr6kw6nz60dcsf2eysaatvxu5aqwa0gn9ttmluk37rh6k3fddxqvhxa25yamn5keq6wpgfyndaadv7pyh6qe0y5ph'
        amount = 2000000
        simple_transaction(receive_address, amount, blockery_api_key, blockery_url)

        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

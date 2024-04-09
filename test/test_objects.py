import unittest
from pytest import mark
from unittest.mock import Mock, patch, MagicMock
from chirpstack_api_wrapper.objects import *

class TestGateway(unittest.TestCase):
    def test_tags_ValueError(self):
        """
        Test Gateway's tags ValueError in init 
        """
        mock_tags = {
            "mock1": 1, # NOT a str
            "mock2": "test2"
        }
        # Init Gateway and Assert Raise
        with self.assertRaises(ValueError) as context:
            Gateway("mock_name", "mock_gateway_id", "mock_tenant_id",tags=mock_tags)

if __name__ == "__main__":
    unittest.main()
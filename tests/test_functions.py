"""Test functions.py"""
import unittest
from unittest.mock import MagicMock

from gcloud_utils import functions

PROJECT = "teste1"
ZONE = "teste2"


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.functions = functions.Functions(PROJECT, ZONE)

    def test_describe_function(self):
        self.functions = MagicMock()
        self.functions__execute_request = MagicMock()

        self.functions.describe_function()

        self.functions.assert_called_once()
        self.functions__execute_request.asser_called_once()
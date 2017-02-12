"""
test_mylife.py - tests for the mylife module
author: mutantmonkey <mutantmonkey@mutantmonkey.in>
"""

import unittest
from mock import MagicMock
from modules import mylife


class TestMylife(unittest.TestCase):
    def setUp(self):
        self.phenny = MagicMock()

    def test_fml(self):
        mylife.fml(self.phenny, None)
        assert self.phenny.say.called is True

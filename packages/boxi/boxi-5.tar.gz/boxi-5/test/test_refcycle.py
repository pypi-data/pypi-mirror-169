import unittest

import boxi.app

class TestReferences(unittest.TestCase):
    def test_func(self):
        app = boxi.app.Application()
        app.register()
        app.activate()
        app.run()

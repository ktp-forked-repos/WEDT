from wedt.tests import *

class TestRankingController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='ranking', action='index'))
        # Test response...

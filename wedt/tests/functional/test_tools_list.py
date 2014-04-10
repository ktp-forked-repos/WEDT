from wedt.tests import *

class TestToolsListController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='tools_list', action='index'))
        # Test response...

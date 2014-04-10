import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from threading import Thread

from wedt.lib.base import BaseController, render
from wedt.controllers.tools_list import ToolsListController
from wedt.model.biotool import BioTool
from wedt.model.article import Article

log = logging.getLogger(__name__)

class RankingController(BaseController):

    def index(self):
        c.tools = ToolsListController.tools
        self.__calculate_rank_points()
        c.tools.sort(cmp=BioTool.compare,
                     reverse=False)
        self.__clear_cache()
        
        return render('/ranking.mako')
    
    def back_to_list(self):
        redirect('/index')
        
    def __calculate_rank_points(self):
        threads = []
        
        for tool in c.tools:
            thread = Thread(target=self.__rank_tool, args=(tool,))
            threads.append(thread)
            thread.start()
            
        for thread in threads:
            thread.join()
        
    @staticmethod
    def __rank_tool(tool):
        tool.get_rank_points()
        
    def __clear_cache(self):
        Article.clear_cache()
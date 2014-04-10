# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from wedt.lib.base import BaseController, render

from wedt.model.biotool import BioTool

log = logging.getLogger(__name__)

class ToolsListController(BaseController):

    tools = []

    def index(self):
        # Return a rendered template
        c.tools = self.tools
        return render('/tools_list.mako')
    
    def clear_tool_list(self):
        while len(self.tools) is not 0:
            self.tools.pop()
            
        redirect('/')
    
    def add_new_tool(self):
        new_tool_name = request.params['new_tool_name']
	if new_tool_name.strip() != '':
            self.tools.append(BioTool(new_tool_name))
        redirect('/')
        
    def delete_tool(self):
        deleted_tool_name = request.params['deleted_tool_name']
        for tool in self.tools:
            if tool.name == deleted_tool_name:
                self.tools.remove(tool)
                redirect('/')
                break
            
    def construct_rank(self):
        redirect('/rank')

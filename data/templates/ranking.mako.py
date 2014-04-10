# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1357925472.666
_enable_loop = True
_template_filename = 'C:\\Users\\piotr\\Dropbox\\PW\\Programming Projects\\WEDT\\wedt\\templates/ranking.mako'
_template_uri = '/ranking.mako'
_source_encoding = 'utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\r\n\t<body>\r\n\t\t<center>\r\n\t\t\t<img src="result.gif">\r\n\t\t\t')
        # SOURCE LINE 5
        __M_writer(escape(h.form(h.url(controller='ranking', action='back_to_list'))))
        __M_writer(u'\r\n\t\t\t')
        # SOURCE LINE 6
        __M_writer(escape(h.submit('go_back', 'Go back to tool list')))
        __M_writer(u'\r\n\t\t\t')
        # SOURCE LINE 7
        __M_writer(escape(h.end_form()))
        __M_writer(u'\r\n\t\t</center>\r\n\r\n\t\t<table width=100% border=1 align="center" cellpadding=5>\r\n\t\t\t<tr>\r\n\t\t\t\t<td><b>Rank place</b></td>\r\n\t\t\t\t<td><b>Name</b></td>\r\n\t\t\t\t<td><b>Google factor</b></td>\r\n\t\t\t\t<td><b>Wikipedia factor</b></td>\r\n\t\t\t\t<td><b>PubMed factor</b></td>\r\n\t\t\t\t<td><b>Total points</b></td>\r\n\t\t\t</tr>\r\n\t\t\t\r\n\t\t\t')
        # SOURCE LINE 20
        place=0 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['place'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\r\n')
        # SOURCE LINE 21
        for tool in c.tools:
            # SOURCE LINE 22
            __M_writer(u'\t\t\t')
            place+=1 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['place'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\r\n\t\t\t<tr>\r\n\t\t\t\t<td>')
            # SOURCE LINE 24
            __M_writer(escape(place))
            __M_writer(u'</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 25
            __M_writer(escape(tool.name))
            __M_writer(u'</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 26
            __M_writer(escape(tool.get_google_points()))
            __M_writer(u'</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 27
            __M_writer(escape(tool.get_wiki_points()))
            __M_writer(u'</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 28
            __M_writer(escape(tool.get_pubmed_points()))
            __M_writer(u'</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 29
            __M_writer(escape(tool.get_rank_points()))
            __M_writer(u'</td>\r\n\t\t\t</tr>\r\n')
        # SOURCE LINE 32
        __M_writer(u'\t\t</table>\r\n\t</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()



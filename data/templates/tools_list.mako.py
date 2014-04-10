# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1357925423.333
_enable_loop = True
_template_filename = 'C:\\Users\\piotr\\Dropbox\\PW\\Programming Projects\\WEDT\\wedt\\templates/tools_list.mako'
_template_uri = '/tools_list.mako'
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
        __M_writer(u'<html>\r\n\t<body>\r\n\t\t<center>\r\n\t\t\t<img src="logo.jpg">\r\n\t\t\t')
        # SOURCE LINE 5
        __M_writer(escape(h.form(h.url(controller='tools_list', action='add_new_tool'), method='post')))
        __M_writer(u'\r\n\t\t\t')
        # SOURCE LINE 6
        __M_writer(escape(h.text('new_tool_name')))
        __M_writer(u'\r\n\t\t\t')
        # SOURCE LINE 7
        __M_writer(escape(h.submit('submit_new_tool', 'Add tool')))
        __M_writer(u'\r\n\t\t\t')
        # SOURCE LINE 8
        __M_writer(escape(h.end_form()))
        __M_writer(u'\r\n\t\t\t\r\n\t\t\t')
        # SOURCE LINE 10
        __M_writer(escape(h.form(h.url(controller='tools_list', action='construct_rank'), method='post')))
        __M_writer(u'\r\n\t\t\t')
        # SOURCE LINE 11
        __M_writer(escape(h.submit('submit_rank', 'Rank tools')))
        __M_writer(u'\r\n\t\t\t')
        # SOURCE LINE 12
        __M_writer(escape(h.end_form()))
        __M_writer(u'\r\n\t\t</center>\r\n\t\t\r\n\t\t<table width=80% border=1 align="center" cellpadding=5>\r\n\t\t\t<tr>\r\n\t\t\t\t<td><b>Tool name<b></td>\r\n\t\t\t\t<td>\r\n\t\t\t\t\t<center>\r\n\t\t\t\t\t\t')
        # SOURCE LINE 20
        __M_writer(escape(h.form(h.url(controller='tools_list', action='clear_tool_list'), method='post')))
        __M_writer(u'\r\n\t\t\t\t\t\t')
        # SOURCE LINE 21
        __M_writer(escape(h.submit('submit_clear_list', 'Clear list')))
        __M_writer(u'\r\n\t\t\t\t\t\t')
        # SOURCE LINE 22
        __M_writer(escape(h.end_form()))
        __M_writer(u'\r\n\t\t\t\t\t</center>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
        # SOURCE LINE 26
        for tool in c.tools:
            # SOURCE LINE 27
            __M_writer(u'\t\t\t<tr>\r\n\t\t\t\t<td>')
            # SOURCE LINE 28
            __M_writer(escape(tool.name))
            __M_writer(u'</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t\t<center>\r\n\t\t\t\t\t\t')
            # SOURCE LINE 31
            __M_writer(escape(h.form(h.url(controller='tools_list', action='delete_tool'), method='post')))
            __M_writer(u'\r\n\t\t\t\t\t\t')
            # SOURCE LINE 32
            __M_writer(escape(h.submit('delete_tool', 'Delete')))
            __M_writer(u'\r\n\t\t\t\t\t\t')
            # SOURCE LINE 33
            __M_writer(escape(h.hidden('deleted_tool_name', value=tool.name)))
            __M_writer(u'\r\n\t\t\t\t\t\t')
            # SOURCE LINE 34
            __M_writer(escape(h.end_form()))
            __M_writer(u'\r\n\t\t\t\t\t</center>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
        # SOURCE LINE 39
        __M_writer(u'\t\t</table>\r\n\t</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()



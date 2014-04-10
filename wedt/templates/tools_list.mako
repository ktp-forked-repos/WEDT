<html>
	<body>
		<center>
			<img src="logo.jpg">
			${h.form(h.url(controller='tools_list', action='add_new_tool'), method='post')}
			${h.text('new_tool_name')}
			${h.submit('submit_new_tool', 'Add tool')}
			${h.end_form()}
			
			${h.form(h.url(controller='tools_list', action='construct_rank'), method='post')}
			${h.submit('submit_rank', 'Rank tools')}
			${h.end_form()}
		</center>
		
		<table width=80% border=1 align="center" cellpadding=5>
			<tr>
				<td><b>Tool name<b></td>
				<td>
					<center>
						${h.form(h.url(controller='tools_list', action='clear_tool_list'), method='post')}
						${h.submit('submit_clear_list', 'Clear list')}
						${h.end_form()}
					</center>
				</td>
			</tr>
			% for tool in c.tools:
			<tr>
				<td>${tool.name}</td>
				<td>
					<center>
						${h.form(h.url(controller='tools_list', action='delete_tool'), method='post')}
						${h.submit('delete_tool', 'Delete')}
						${h.hidden('deleted_tool_name', value=tool.name)}
						${h.end_form()}
					</center>
				</td>
			</tr>
			% endfor
		</table>
	</body>
</html>
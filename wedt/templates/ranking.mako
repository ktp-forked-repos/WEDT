<html>
	<body>
		<center>
			<img src="result.gif">
			${h.form(h.url(controller='ranking', action='back_to_list'))}
			${h.submit('go_back', 'Go back to tool list')}
			${h.end_form()}
		</center>

		<table width=100% border=1 align="center" cellpadding=5>
			<tr>
				<td><b>Rank place</b></td>
				<td><b>Name</b></td>
				<td><b>Google factor</b></td>
				<td><b>Wikipedia factor</b></td>
				<td><b>PubMed factor</b></td>
				<td><b>Total points</b></td>
			</tr>
			
			<% place=0 %>
			%for tool in c.tools:
			<% place+=1 %>
			<tr>
				<td>${place}</td>
				<td>${tool.name}</td>
				<td>${tool.get_google_points()}</td>
				<td>${tool.get_wiki_points()}</td>
				<td>${tool.get_pubmed_points()}</td>
				<td>${tool.get_rank_points()}</td>
			</tr>
			%endfor
		</table>
	</body>
</html>
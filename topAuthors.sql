Select 
		au.name,
		count(*) as total
		

from log l
inner join articles ar on concat('/article/',ar.slug) = l.path
inner join authors au on au.id = ar.author
	--and b.id = 27
group by au.name
order by total desc
Select 
		a.path,
		b.slug,
		count(*) as total
		

from log a
inner join articles b on concat('/article/',b.slug) = a.path

	--and b.id = 27
group by a.path,
		b.slug
order by total desc
limit 3;
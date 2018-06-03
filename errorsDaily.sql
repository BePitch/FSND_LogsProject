--Build query to output details around errors. Additional columns are in query for future scaling scope in business needs 
--Will only invoke column 1 and 5 for this project

select
		l.time::timestamp::date as errorDate,
		count(*)totalDailyRequests,
		sum(case when l.status ='200 OK' then 1 else 0 end) as totalSuccess,
		sum(case when l.status ='404 NOT FOUND' then 1 else 0 end) as totalErrors,
		Cast((sum(case when l.status ='404 NOT FOUND' then 1 else 0 end)::float / count(*)::float)* 100 as decimal(10,2)) as PercentError
		
from log l
group by  l.time::timestamp::date

--constraint to only output days greater than 0.01 error rate
having sum(case when l.status ='404 NOT FOUND' then 1 else 0 end)::float/count(*)::float >=.01





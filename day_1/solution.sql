WITH cte as (
SELECT X.*, Y.total_time_spent FROM 
(
SELECT
a.*
from activities a
)as X
JOIN
(
SELECT
user_id,
sum(time_spent)as total_time_spent
FROM
activities a
where activity_type in ('send','open')
group by 1
)Y
on (X.user_id = Y.user_id)
)


select 
DB.age_bucket,
ROUND(SUM(CASE WHEN activity_type = 'send' THEN (time_spent/total_time_spent)*100.0 END), 2) as send_perc,
ROUND(SUM(CASE WHEN activity_type = 'open' THEN (time_spent/total_time_spent)*100.0 END), 2) as open_perc
FROM
cte as DA
JOIN age_breakdown as DB
on (DA.user_id =DB.user_id)
GROUP BY 1
